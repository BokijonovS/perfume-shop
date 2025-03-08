from django.contrib import admin
from .models import Category, Specifications, Product, ProductImage


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_display_links = ('id',)
    list_editable = ('name', 'slug',)

class ProductSizeInline(admin.TabularInline):
    model = Specifications
    extra = 1  # Number of empty slots for new entries
    fields = ['id', 'text']  # Fields to display in the inline form


class ProductImageInline(admin.TabularInline):  # or admin.StackedInline for a different style
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeInline, ProductImageInline]
    list_display = ['id', 'name', 'count', 'price', 'color', 'size']
    prepopulated_fields = {'slug': ('name','color')}
    list_display_links = ['id', 'name']
    list_editable = ['count', 'price', 'color', 'size']
    search_fields = ['name', 'price', 'color', 'size']

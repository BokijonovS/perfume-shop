from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        ordering = ['-id']


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    rating = models.FloatField(default=3.7)
    count = models.IntegerField()
    price = models.FloatField()
    size = models.CharField(max_length=100)
    description = models.TextField(null=True)

    @property
    def main_image(self):
        """Returns the first image URL or None if no images exist."""
        first_image = self.images.first()
        return first_image.image.url if first_image else None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.name}"


class Specifications(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="specifications")
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Specifications"


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes_dislikes')
    is_like = models.BooleanField(default=True)  # True for like, False for dislike

    def __str__(self):
        return f'{self.product} {self.is_like}'







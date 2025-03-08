from django.shortcuts import render

from shop.models import Product


# Create your views here.

def home(request):
    product = Product.objects.first()
    context = {
        'product': product
    }
    return render(request, template_name='index.html', context=context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }
    return render(request, "product_detail.html", context=context)

from django.urls import path
from .views import home, product_detail

urlpatterns = [
    path('', home,  name="home"),
    path('product/<slug:slug>', product_detail,  name="home")
]

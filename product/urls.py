from django.urls import path
from product.views import products


urlpatterns = [
    path("", products, name="products")
]
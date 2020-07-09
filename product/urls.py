from django.urls import path
from product.views import products


urlpatterns = [
    path("all/", products, name="products")
]
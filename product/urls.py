from django.urls import path
from product.views import *


urlpatterns = [
    path("all/", products, name="products"),
    path("<int:id>/", product, name="product"),
    path("create/", product_create, name="product-create"),
    path("edit/<int:id>/", product_edit, name="product-edit"),
    path("delete/<int:id>/", product_delete, name="product-delete"),
]

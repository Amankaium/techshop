from django.urls import path
from product.views import *


urlpatterns = [
    path("all/", products, name="products"),
    path("category/<int:pk>/", category, name="category"),
    path("category/create/", CategeryCreate.as_view(), name="category-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("create-few/", create_few, name="product-create-few"),
    path("edit/<int:id>/", product_edit, name="product-edit"),
    path("delete/<int:id>/", product_delete, name="product-delete"),
]

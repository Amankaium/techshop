from django.db import models
from product.models import Product


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="product_in_order")

    product = models.ForeignKey(
        to=Product, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="product_in_order")

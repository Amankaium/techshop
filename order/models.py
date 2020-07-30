from django.db import models
from product.models import Product


class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product_in_order",
        verbose_name="Заказ")

    product = models.ForeignKey(
        to=Product, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="product_in_order",
        verbose_name="Товар")

    added = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name="Время добавления"
    )
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название")

    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
        blank=True,
        verbose_name="Категория"
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="product_images",
        verbose_name="Изображение товара",
        default="static/no_image.png"
    )

    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")

    price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name="Цена")

    sales = models.IntegerField(
        default=0, verbose_name="Кол-во продаж")

    avialable = models.BooleanField(
        default=True, verbose_name="Есть в наличии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "Товары"


class Category(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

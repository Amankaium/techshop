from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название")

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    parent_category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="child_category"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

from django.db import models
from django.contrib.auth.models import User

class FeedBack(models.Model):
    name = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name="Ваше имя"
    )

    text = models.TextField(
        null=True, blank=True,
        verbose_name="Текст обращения"
    )

    screen = models.ImageField(
        upload_to="feedback",
        null=True, blank=True,
        verbose_name="Приложенное изображение"
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Формы обратной связи"

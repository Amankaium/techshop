from django.contrib import admin
from .models import FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    # model = FeedBack
    list_display = ["id", "name", "text", "screen", "user", "date", "phone", "email"]
    





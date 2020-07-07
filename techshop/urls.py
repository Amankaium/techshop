from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include("product.urls")),
    path('feedback', include("feedback.urls")),
    path("", include("core.urls")),
]

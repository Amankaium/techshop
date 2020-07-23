from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("sellers/", sellers, name="sellers"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("registration/", registration, name="registration"),
    path("change-password/", change_password, name='change-password'),
    path("profile/<int:pk>/", profile, name="profile"),
]
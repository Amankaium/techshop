from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("test/", test, name="test"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("registration/", registration, name="registration")
]
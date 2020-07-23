from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ChangePasswordForm(forms.Form):
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)

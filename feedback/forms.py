from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    # text = forms.TextInput(attrs={"rows": "3"})
    class Meta:
        model = FeedBack
        fields = ["name", "text", "screen", "phone", "email"]
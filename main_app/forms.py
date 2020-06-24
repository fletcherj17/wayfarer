from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import date

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    current_city = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('name', 'current_city', 'username', 'password1', 'password2')
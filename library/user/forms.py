from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreatingForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

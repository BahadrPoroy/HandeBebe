from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm


class UserSigninForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUserModel
        fields = ('username', 'password')

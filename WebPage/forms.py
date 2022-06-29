from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignupForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
        ))

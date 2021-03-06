from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}), max_length=254)
    password = forms.CharField(widget=forms.PasswordInput, max_length=254)

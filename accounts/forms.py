from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputUsername'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputFirstName'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputLastName'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPasswordConfirm'}),
        }

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")
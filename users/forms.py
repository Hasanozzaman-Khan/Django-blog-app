from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


"""User Registration form"""
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']


"""profile update form related to User"""
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'email']


"""profile update form related to Profile (profile picture)"""
class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image']

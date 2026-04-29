from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import customUser

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = ('username', 'email', 'phone_number')

class customUserChangeForm(UserChangeForm):
    class Meta:
        model = customUser
        fields = ('username',)
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import customUser, userProfile

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = ('username', 'email',)

class UserProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = userProfile
        fields = ['phone_number', 'bio', 'shipping_address', 'image']

class passwordresetForm(forms.ModelForm):
    class Meta:
        model = customUser
        fields = ('email',)
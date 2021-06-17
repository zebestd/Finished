from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Usta








class UstaForm(ModelForm):
    class Meta:
         model = Usta
         fields = ('isim', 'kategori', 'il','ilce', 'website', 'eposta', 'aciklama', 'telefon', 'resim')


         
    


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Usta
        fields = ['isim', 'eposta', 'kategori', 'il','ilce', 'website', 'aciklama', 'telefon', 'resim']



 
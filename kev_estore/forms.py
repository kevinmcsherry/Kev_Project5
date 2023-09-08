from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GolfGear
from django import forms
from django.forms import ModelForm



class AddProductForm(forms.ModelForm):
    name = forms.TextInput();
    price = forms.TextInput();
    image = forms.ImageField();

    class Meta:
        model = GolfGear
        fields = '__all__'

class CustomerReviewForm(forms.ModelForm):
    feedback = forms.TextInput();




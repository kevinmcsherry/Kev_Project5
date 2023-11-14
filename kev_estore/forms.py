from .models import GolfGear
from django import forms


class AddProductForm(forms.ModelForm):

    name = forms.TextInput()
    price = forms.TextInput()
    image = forms.ImageField()

    class Meta:

        model = GolfGear
        fields = '__all__'


class CustomerReviewForm(forms.ModelForm):

    feedback = forms.TextInput()

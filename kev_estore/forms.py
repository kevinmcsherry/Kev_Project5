from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GolfGear
from django import forms
from crispy_forms.helper import FormHelper

class ProductForm(forms.ModelForm):

    class Meta:
        model = GolfGear
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        names = GolfGear.objects.all()

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'




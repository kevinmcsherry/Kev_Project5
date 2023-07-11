from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, User


#class CreateAccount(UserCreationForm):
    #birthdate = forms.DateField()
    #email = forms.CharField(widget=EmailInput)
    #name = forms.CharField(max_length=100)

    #class Meta:
        #model = User
        #fields = ["username", "password1", "password2"]
        #model = Customer
        #fields = ["name", "email", "username"]
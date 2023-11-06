from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy


# Create your views here.

class Login(SuccessMessageMixin, LoginView):
    '''
    Recieve login details from registered user
    if user details are recognised, bring them
    to the main Website product page
    if not recognised, return to Login page
    '''
    template_name = 'kev_estore/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Login successful!"
    
    def get_success_url(self):
        return reverse_lazy('golfgear')

class Logout(LogoutView):
    '''
    Recieves a logout instruction
    returns user to the Logout page
    '''
    template_name = 'kev_estore/logout.html'
    redirect_authenticated_user = True
    success_message = "Logout successful!"
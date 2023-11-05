from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

path('login/', Login.as_view(), name='login'),
path('logout/', Logout.as_view(), name='logout'),
]

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import login
from .models import *

# Create your views here.

class Login(SuccessMessageMixin, LoginView):
    template_name = 'shop_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Login Successful"
    
    def get_success_url(self):
        return reverse_lazy('tasks')
        

class CreateAccount(SuccessMessageMixin, FormView):
    template_name = 'shop_app/create_account.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_message = "Account Created Successfully"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateAccount, self).form_valid(form)

    def state(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(CreateAccount, self).get(*args, **kwargs)



def home(request):
	context = {}
	return render(request, 'kev_estore/home_page.html', context)

def clothes(request):
	clothings = Clothing.objects.all()
	context = {'clothings':clothings}
	return render(request, 'kev_estore/clothes.html', context)

def accessories(request):
	accessories = Accessories.objects.all()
	context = {'accessories':accessories}
	return render(request, 'kev_estore/accessories.html', context)

def clubs(request):
	clubs = Clubs.objects.all()
	context = {'clubs':clubs}
	return render(request, 'kev_estore/clubs.html', context)

def basket(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_num':0}

    context ={'items':items, 'order':order}
    return render(request, 'kev_estore/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_num':0}

    context ={'items':items, 'order':order}
    return render(request, 'kev_estore/checkout.html', context)


def page_not_found(request, exception):
    return render(request, 'kev_estore/page_not_found.html', status=404)
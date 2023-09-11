from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import *
from django.db import models
from django.http import JsonResponse
import json
import datetime
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings
import re
from kev_estore.forms import AddProductForm


class Login(SuccessMessageMixin, LoginView):
    template_name = 'kev_estore/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Login successful!"
    
    def get_success_url(self):
        return reverse_lazy('golfgear')

class Logout(LogoutView):
    template_name = 'kev_estore/logout.html'
    redirect_authenticated_user = True
    success_message = "Logout successful!"
    
    
         
class CreateAccount(SuccessMessageMixin, FormView):
    template_name = 'kev_estore/create_account.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_message = "Account created successfully!"
    success_url = reverse_lazy('golfgear')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CreateAccount, self).form_valid(form)
        

    @receiver(post_save, sender=User)
    def create_or_update_customer(sender, instance, created, **kwargs):
        """Create or update the Customer"""
        if created:
            cust_name = str(instance)
            Customer.objects.create(user=instance, name=cust_name, email=cust_name + "1979@gmail.com")
        instance.customer.save()
    

    def state(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('golfgear')
        return super(CreateAccount, self).get(*args, **kwargs)


def home(request):
	context = {}
	return render(request, 'kev_estore/home_page.html', context)

def logout(request):
    context = {}
    return render(request, 'kev_estore/logout.html', context)

def purchase_complete(request):
    context = {}
    return render(request, 'kev_estore/purchase_complete.html', context)

def update_golfgear(request):
    golfgears = GolfGear.objects.all()
    context = {'golfgears':golfgears}
    return render(request, 'kev_estore/update_golfgear.html', context)

def delete_golfgear(request):
    golfgears = GolfGear.objects.all()
    context = {'golfgears':golfgears}
    return render(request, 'kev_estore/golfgear_confirm_delete.html', context)

def golfgear(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_num
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_num':0, 'shipping':False}
        basketItems = order['get_basket_num']
    
    golfgears = GolfGear.objects.all()
    context = {'golfgears':golfgears, 'basketItems':basketItems}
    return render(request, 'kev_estore/golfgear.html', context)


def basket(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_num
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_num':0, 'shipping':False}
        basketItems = order['get_basket_num']

    context ={'items':items, 'order':order, 'basketItems':basketItems}
    return render(request, 'kev_estore/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_num
    else:
        items = []
        order = {'get_basket_total':0, 'get_basket_num':0, 'shipping':False}
        basketItems = order['get_basket_num']

    context ={'items':items, 'order':order, 'basketItems':basketItems}
    return render(request, 'kev_estore/checkout.html', context)


def page_not_found(request, exception):
    return render(request, 'kev_estore/page_not_found.html', status=404)

def updateItem(request):
    data = json.loads(request.body)
    golfgearId = data['golfgearId']
    action = data['action']

    customer = request.user.customer
    golfgear = GolfGear.objects.get(id=golfgearId)
    order, created = Order.objects.get_or_create(customer=customer, done=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, golfgear=golfgear)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    order_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
	    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, done=False)
    total = (data['form']['total'])
    order.order_id = order_id
    order.done = True
    order.save()

    if order.shipping == True:
        DeliveryAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        county=data['shipping']['county'],
        country=data['shipping']['country'],
        post_code=data['shipping']['postalcode'],
        )

    else:
        print('User is not logged in')
    success_message = "Transaction Complete"
    return JsonResponse('Payment Complete!', safe=False)

def newsletter(request):
    if request.method == 'POST':
            post_data = request.POST.copy()
            email = post_data.get("email", None)
            name = post_data.get("name", None)
            subscribedUsers = SubscribedUsers()
            subscribedUsers.email = email
            subscribedUsers.name = name
            subscribedUsers.save()
            # send a confirmation mail
            subject = 'NewsLetter Subscription'
            message = 'Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
    return render(request, 'kev_estore/newsletter.html')

def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        re = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email = email):
        re = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        re = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        re = JsonResponse({'msg': 'Thank you for signing up'})
    return re

def product_management(request):
    context = {}
    return render(request, 'kev_estore/product_management.html', context)


def add_product(request):
    if request.POST:
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(product_management)      
        redirect_authenticated_user = True
        success_message = "Product Added!" 
    return render(request, 'kev_estore/add_product.html', {'form' : AddProductForm})

class UpdateProduct(SuccessMessageMixin, UpdateView):
    model = GolfGear
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Item updated successfully"
    success_url = reverse_lazy('product_management')
    

class DeleteProduct(SuccessMessageMixin, DeleteView):
    model = GolfGear
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Item deleted successfully"
    success_url = reverse_lazy('product_management')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteProduct, self).delete(request, *args, **kwargs)



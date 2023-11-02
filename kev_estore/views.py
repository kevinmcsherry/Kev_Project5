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

    
         
class CreateAccount(SuccessMessageMixin, FormView):
    '''
    Creates a new account by receiving the parameters : -
    Username
    Password
    Password(confirmed)
    On success, class will bring user to main page of Website
    with successful message.
    On error, class will return user to the 'create account' form.
    '''
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
    '''
    Link to home page
    '''
    context = {}
    return render(request, 'kev_estore/home_page.html', context)

def logout(request):
    '''
    Link to Logout page
    '''
    context = {}
    return render(request, 'kev_estore/logout.html', context)

def purchase_complete(request):
    '''
    Link to purchase complete page
    '''
    context = {}
    return render(request, 'kev_estore/purchase_complete.html', context)

def update_golfgear(request):
    '''
    Recieves the instruction from user
    to update product from the product management 
    page
    Brings user to update product form
    '''
    golfgears = GolfGear.objects.all()
    context = {'golfgears':golfgears}
    return render(request, 'kev_estore/update_golfgear.html', context)

def delete_golfgear(request):
    '''
    Recieves the instruction from user
    to delete product from the product management 
    page
    Brings user to delete product form
    '''
    golfgears = GolfGear.objects.all()
    context = {'golfgears':golfgears}
    return render(request, 'kev_estore/golfgear_confirm_delete.html', context)

def golfgear(request):
    '''
    Renders main product page
    Based on the user credentials
    and past interactions, will
    have the basket populated
    '''

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
    '''
    Recieves user information
    Basket will set number based on 
    previous visit if any.
    If new, basket will be reset.
    '''
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
    '''
    Recieves user information
    Recieves basket item count
    Recieves basket total
    Renders checkout page with details
    of order
    '''
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
    '''
    Triggers custom page not found
    when an unrecognised page is navigated
    '''
    return render(request, 'kev_estore/page_not_found.html', status=404)

def updateItem(request):
    '''
    This function is to allow user
    to add or subtract the quantity 
    of items in basket for products
    present.
    It will recieve items from basket,
    display each product, item counts
    and overall cost amount.
    The user can use the arrow keys to 
    increase or decrease item amounts.
    Will delete the item if count is <0.
    '''
    data = json.loads(request.body)
    golfgearId = data['golfgearId']
    action = data['action']

    customer = request.user.customer
    golfgear = GolfGear.objects.get(id=golfgearId)
    order, created = Order.objects.get_or_create(customer=customer, done=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, golfgear=golfgear)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
        messages.success(request, "Item Added to Basket")
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
        messages.success(request, "Item Removed from Basket")
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    '''
    Recieves details of order
    Once transaction is completed via
    PayPal, stores data in database
    '''
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
    return JsonResponse('Payment Complete!', safe=False)

def newsletter(request):
    '''
    Link to Newsletter signup
    form
    '''
    context = {}       
    return render(request, 'kev_estore/newsletter.html')

def product_management(request):
    '''
    Link to Product management
    page
    '''
    context = {}
    if request.user.is_superuser:
        return render(request, 'kev_estore/product_management.html', context)
    else:      
        return redirect('login')
        


def add_product(request):
    '''
    Request for an addition of a product
    Renders add product form
    Takes inputs of name, cost, image
    Stores new product info
    Displays new product info
    on product page
    '''
    if request.user.is_superuser:
        if request.POST:
            form = AddProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect(product_management)      
            redirect_authenticated_user = True
            success_message = "Product Added!" 
        return render(request, 'kev_estore/add_product.html', {'form' : AddProductForm})
    else:
        return redirect('login')

class UpdateProduct(SuccessMessageMixin, UpdateView):
    '''
    Recieves instruction to update
    products
    Renders Product page with update
    option on each current product
    Once product selected, uses item id
    to identify selection - form renders
    to allow for updated details
    Renders product page with updated details
    of products
    Stored update in database
    '''
    model = GolfGear
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Item updated successfully"
    success_url = reverse_lazy('product_management')

class DeleteProduct(SuccessMessageMixin, DeleteView):
    '''
    Recieves instruction to delete
    products
    Renders Product page with delete
    option on each current product
    Once product selected, uses item id
    to identify selection - form renders
    to allow for updated details
    Renders product page with updated details
    of products - product deleted not present
    Stored update in database
    '''
    model = GolfGear
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Item deleted successfully"
    success_url = reverse_lazy('product_management')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteProduct, self).delete(request, *args, **kwargs)



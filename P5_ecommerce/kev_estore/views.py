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
from django.http import JsonResponse
import json
import datetime

# Create your views here.

class Login(SuccessMessageMixin, LoginView):
    template_name = 'kev_estore/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_message = "Login Successful"
    
    def get_success_url(self):
        return reverse_lazy('tasks')
        

class CreateAccount(SuccessMessageMixin, FormView):
    template_name = 'kev_estore/create_account.html'
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

#def accessories(request):
	#accessories = Accessories.objects.all()
	#context = {'accessories':accessories}
	#return render(request, 'kev_estore/accessories.html', context)

#def clubs(request):
	#clubs = Clubs.objects.all()
	#context = {'clubs':clubs}
	#return render(request, 'kev_estore/clubs.html', context)

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
    print('Action', action)
    print('golfgearId', golfgearId)

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

    return JsonResponse('Payment Complete!', safe=False)
from django.shortcuts import render
from checkout.models import Order, OrderItem
import json
import datetime
from django.http import JsonResponse
from django.contrib import messages
from kev_estore.models import GolfGear
from checkout.models import DeliveryAddress

# Create your views here.


def purchase_complete(request):
    '''
    Link to purchase complete page
    '''

    context = {}
    return render(request, 'purchase_complete.html', context)


def basket(request):
    '''
    Recieves user information
    Basket will set number based on
    previous visit if any.
    If new, basket will be reset.
    '''

    if request.user.is_authenticated:
        customer = request.user.customer
        (order, created) = \
            Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_num
    else:
        items = []
        order = {'get_basket_total': 0, 'get_basket_num': 0,
                 'shipping': False}
        basketItems = order['get_basket_num']

    context = {'items': items, 'order': order,
               'basketItems': basketItems}
    return render(request, 'basket.html', context)


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
        (order, created) = \
            Order.objects.get_or_create(customer=customer, done=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_num
    else:
        items = []
        order = {'get_basket_total': 0, 'get_basket_num': 0,
                 'shipping': False}
        basketItems = order['get_basket_num']

    context = {'items': items, 'order': order,
               'basketItems': basketItems}
    return render(request, 'checkout.html', context)


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
        (order, created) = \
            Order.objects.get_or_create(customer=customer, done=False)
        total = data['form']['total']
        order.order_id = order_id
        order.done = True
        order.save()

    if order.shipping is True:
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
    (order, created) = Order.objects.get_or_create(customer=customer,
                                                   done=False)

    (orderItem, created) = OrderItem.objects.get_or_create(order=order,
                                                           golfgear=golfgear)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
        messages.success(request, 'Item Added to Basket')
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
        messages.success(request, 'Item Removed from Basket')
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from checkout.models import GolfGear
from django.http import JsonResponse
import json
from kev_estore.forms import AddProductForm
from checkout.models import Order, OrderItem


def home(request):
    '''
    Link to home page
    '''

    context = {}
    return render(request, 'kev_estore/home_page.html', context)


def update_golfgear(request):
    '''
    Recieves the instruction from user
    to update product from the product management 
    page
    Brings user to update product form
    '''

    golfgears = GolfGear.objects.all()
    context = {'golfgears': golfgears}
    return render(request, 'kev_estore/update_golfgear.html', context)


def delete_golfgear(request):
    '''
    Recieves the instruction from user
    to delete product from the product management 
    page
    Brings user to delete product form
    '''

    golfgears = GolfGear.objects.all()
    context = {'golfgears': golfgears}
    return render(request, 'kev_estore/golfgear_confirm_delete.html',
                  context)


def golfgear(request):
    '''
    Renders main product page
    Based on the user credentials
    and past interactions, will
    have the basket populated
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

    golfgears = GolfGear.objects.all()
    context = {'golfgears': golfgears, 'basketItems': basketItems}
    return render(request, 'kev_estore/golfgear.html', context)


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


def product_management(request):
    '''
    Link to Product management
    page
    '''

    context = {}
    if request.user.is_superuser:
        return render(request, 'kev_estore/product_management.html',
                      context)
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
            success_message = 'Product Added!'
        return render(request, 'kev_estore/add_product.html',
                      {'form': AddProductForm})
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
    success_message = 'Item updated successfully'
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
    success_message = 'Item deleted successfully'
    success_url = reverse_lazy('product_management')

    def delete(
        self,
        request,
        *args,
        **kwargs
        ):

        messages.success(self.request, self.success_message)
        return super(DeleteProduct, self).delete(request, *args,
                **kwargs)

from django.db import models
from users.models import Customer
from kev_estore.models import GolfGear

# Create your models here.

class Order(models.Model):
    '''
    Table to store all orders
    Helps to render data on pages
    in regards to shipping, basket totals
    etc
    '''
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, null=True, blank=False)
    order_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        orderitems = self.orderitem_set.all()
        return shipping


    @property
    def get_basket_num(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_basket_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    '''
    Table to host the individual items within orders
    Helps in deriving totals for orders
    '''
    golfgear = models.ForeignKey(GolfGear, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
		    total = self.golfgear.price * self.quantity
		    return total

class DeliveryAddress(models.Model):
    '''
    Table to host delivery details of orders made
    '''
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    post_code = models.CharField(max_length=100, null=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.address 

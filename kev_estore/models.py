from django.db import models
from users.models import Customer


class GolfGear(models.Model):
    '''
    Table to host all data on products
    Current and newly added
    '''
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
                url = self.image.url
        except:
                url = ''
        return url

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

class SubscribedUsers(models.Model):
    '''
    Table to host data on customers registered for newsletter
    '''
    email = models.CharField(unique=True, max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)


from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Clothing(models.Model):
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

class Accessories(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
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

class Clubs(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
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
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, null=True, blank=False)
    order_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_basket_num(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.item_num for item in orderitems])
        return total

    @property
    def get_basket_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    

class OrderItem(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.SET_NULL, blank=True, null=True)
    clothing_quantity = models.IntegerField(default=0, null=True, blank=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.SET_NULL, blank=True, null=True)
    accessories_quantity = models.IntegerField(default=0, null=True, blank=True)
    clubs = models.ForeignKey(Clubs, on_delete=models.SET_NULL, blank=True, null=True)
    clubs_quantity = models.IntegerField(default=0, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)

    @property
    def item_num(self):
        if self.clothing is None and self.clubs is None and self.accessories is None:
            total = 0
        elif self.clubs is None and self.accessories is None:
            total = self.clothing_quantity
        elif self.accessories is None and self.clothing is None:
            total = self.clubs_quantity
        elif self.clothing is None:
            total = (self.clubs_quantity + self.accessories_quantity)
        elif self.clubs is None:
            total = (self.clothing_quantity + self.accessories_quantity)
        elif self.accessories is None:
            total = (self.clubs_quantity + self.clothing_quantity)
        else:
            total = (self.clubs_quantity + self.clothing_quantity + self.accessories_quantity)
        return total

    @property
    def get_total(self):
        if self.clothing is None and self.clubs is None and self.accessories is None:
            total = 0
        elif self.clubs is None and self.accessories is None:
            total = self.clothing.price
        elif self.accessories is None and self.clothing is None:
            total = self.clubs.price
        elif self.clothing is None:
            total = (self.clubs.price + self.accessories.price)
        elif self.clubs is None:
            total = (self.clothing.price + self.accessories.price)
        elif self.accessories is None:
            total = (self.clubs.price + self.clothing.price)
        else:
            total = (self.clubs.price + self.clothing.price + self.accessories.price)
        return total

    #def __tuple__(self):
        #return (self.clothing.name, self.accessories.name, self.clubs.name)

class DeliveryAddress(models.Model):
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
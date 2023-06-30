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

class OrderItem(models.Model):
    clothing = models.ForeignKey(Clothing, on_delete=models.SET_NULL, blank=True, null=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.SET_NULL, blank=True, null=True)
    clubs = models.ForeignKey(Clubs, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = (self.clothing.price + self.clubs.price + self.accessories.price) * self.quantity
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
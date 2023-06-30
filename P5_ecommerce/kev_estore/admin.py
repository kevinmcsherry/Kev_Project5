from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Clothing)
admin.site.register(Clubs)
admin.site.register(Accessories)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)


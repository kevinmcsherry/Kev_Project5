from django.contrib import admin
from .models import *

admin.site.register(SubscribedUsers)
admin.site.register(Customer)
admin.site.register(GolfGear)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Customer

@receiver(post_save, sender=user)
def create_or_update_customer(sender, **kwargs):
    print(instance)
"""Create or update the Customer"""
    if created:
        Customer.objects.create(user=instance, name=instance, email="xxx@xxx.com")
    instance.customer.save()
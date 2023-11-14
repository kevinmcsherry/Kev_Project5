from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

//@receiver(post_save, sender=User)
@receiver(request_finished)
def create_or_update_customer(sender, instance, created, **kwargs):
    print(user)
"""Create or update the Customer"""
    if created:
        Customer.objects.create(user=instance, name=instance, email="xxx@xxx.com")
    instance.customer.save()
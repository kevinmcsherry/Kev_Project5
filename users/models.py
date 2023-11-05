from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    '''
    Table to host data of all registered customers
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


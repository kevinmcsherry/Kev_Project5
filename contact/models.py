from django.db import models

# Create your models here.


class SubscribedUsers(models.Model):
    '''
    Table to host data on customers registered for newsletter
    '''
    email = models.CharField(unique=True, max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

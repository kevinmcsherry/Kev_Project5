from django.db import models


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
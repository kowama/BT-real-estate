from django.db import models
from datetime import datetime
from realtors.models import Realtor
from .choices import state_choices_tuple


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=state_choices_tuple)
    zip_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    square_feet = models.IntegerField()
    lot_size = models.DecimalField(max_digits=6, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/listings/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/listings/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/listings/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/listings/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/listings/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/listings/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/listings/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_day = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

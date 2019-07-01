from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/realtors/%y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    hire_date = models.DateField(default=datetime.now)
    is_mvp = models.BooleanField(default=False)

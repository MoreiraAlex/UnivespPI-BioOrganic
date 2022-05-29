from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.IntegerField(('phone'),default= 0)
    insta = models.CharField(name='insta',max_length=30, default= '')
    address = models.CharField(name='address',max_length=50, default= '')
    discard = models.BooleanField(name='discard',default= False)
    time = models.CharField(name='time',max_length=50, default= '')


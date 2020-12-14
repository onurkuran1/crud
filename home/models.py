from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=11)
    identificationNumber = models.CharField(max_length=11)


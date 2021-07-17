from django.db import models

# Create your models here.


class Customer(models.Model):
    no = models.CharField(max_length=120)
    name = models.TextField()
    adress = models.TextField()

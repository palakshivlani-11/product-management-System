from django.db import models

# Create your models here.

class product(models.Model):
    size = models.CharField(null=True,blank=True,max_length=50)
    modelno = models.CharField(null=True,blank=True,max_length=50)
    water = models.CharField(null=True,blank=True,max_length=50)
    gas = models.CharField(null=True,blank=True,max_length=50)
    air = models.CharField(null=True,blank=True,max_length=50)
    wpf = models.CharField(null=True,blank=True,max_length=50)
    density = models.CharField(null=True,blank=True,max_length=50)
    vescosity = models.CharField(null=True,blank=True,max_length=50)
    temp = models.CharField(null=True,blank=True,max_length=50)
    pressure = models.CharField(null=True,blank=True,max_length=50)
    distance = models.CharField(null=True,blank=True,max_length=50)
    price = models.IntegerField(null=True,blank=True)
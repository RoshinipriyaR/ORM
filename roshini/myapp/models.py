from django.db import models

class Bike_Service(models.Model):
    Service_No = models.IntegerField()
    Customer_Name = models.CharField(max_length=20)
    Bike_Model = models.CharField(max_length=20)
    Service_Date = models.DateField()
    Service_Cost = models.FloatField()
    Address = models.TextField()
    Service_Type = models.CharField(max_length=30)
   
    from django.contrib import admin
from .models import Bike_Service

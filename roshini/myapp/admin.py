from django.contrib import admin
from .models import Bike_Service

class Bike_ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "Service_No",
        "Customer_Name",
        "Bike_Model",
        "Service_Date",
        "Service_Cost",
        "Address",
        "Service_Type"
    ]

admin.site.register(Bike_Service, Bike_ServiceAdmin)
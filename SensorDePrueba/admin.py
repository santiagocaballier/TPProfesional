from django.contrib import admin
from .models import Sensor,DataSensor

# Register your models here.
admin.site.register(Sensor)
admin.site.register(DataSensor)

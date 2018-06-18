from django.db import models

# Create your models here.
class Sensor(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class DataSensor(models.Model):
    sensor =  models.ForeignKey(Sensor,on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    data = models.FloatField()
    
    def __str__(self):
        return str(self.datetime) + ' - ' + str(self.data)
    
    
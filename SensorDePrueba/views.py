
from .models import DataSensor, Sensor
from django.http import HttpResponse
from django.template import Context, loader 
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core import serializers
import json
from datetime import datetime
# Create your views here.

def get_data_sensor(request,sensor_nombre):
    dq = DataSensor.objects.filter(sensor__nombre=sensor_nombre)
    
    ds = serializers.serialize("json",dq)   
    
    template = loader.get_template('dashboard/dashboard.html')
    
    obj = []
    for d in dq:
        obj.append({'datetime' : str(d.datetime.date()) + ' ' + str(d.datetime.time()),'value' : d.data })
    
    print(obj)
       
    context = {
        'ctx_ds' : ds,
        'ctx_sensor_nombre' : sensor_nombre,
        'ctx_data' : obj
    }
    
    return render(request,'dashboard/dashboard.html',context)


def set_data_sensor(request,sensor_nombre,dataint,datadec):
    result = 'FAIL\n'
    
    qsensor = Sensor.objects.filter(nombre=sensor_nombre)
    if qsensor:
        sensor = qsensor[0] 
    
        dsen = DataSensor()
        dsen.data = float(str(dataint) + '.' + str(datadec))
        dsen.datetime = datetime.now()
        dsen.sensor = sensor    
        
        dsen.save()
        print(dsen)
        result = 'OK\n'
        
    return HttpResponse(result)
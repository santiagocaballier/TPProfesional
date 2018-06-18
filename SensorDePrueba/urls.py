
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic.base import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    path('get_data_sensor/<str:sensor_nombre>', views.get_data_sensor),
    path('set_data_sensor/<str:sensor_nombre>/<int:dataint>.<int:datadec>',views.set_data_sensor)

]


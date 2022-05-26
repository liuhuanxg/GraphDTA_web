#-*-coding:utf-8 -*-

from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('upload_data_set/', upload_data_set),
]

app_name = "home"
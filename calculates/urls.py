from django.urls import path

from . import views


app_name = 'calculates'

urlpatterns = [
    path('', views.entry, name='entry'),
    
]

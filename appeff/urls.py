from django.urls import path
from . import views

urlpatterns = [
    path('empezar-viaje', views.EmpezarViaje, name='empezar-viaje'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('empezar-viaje', views.EmpezarViaje, name='empezar-viaje'),
    path('culminar-viaje/<int:id>', views.CulminarViaje, name='culminar-viaje'),
]

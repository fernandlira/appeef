from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conductor(models.Model):
    STATUS = ((0, "Dispoible"), (1, "No disponible"))
    id = models.Autofield(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilidad = models.IntegerField(default=0, choices=STATUS)


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    modelo = models.charField(max_length=30)
    placa = models.charField(max_length=10)
    anno = models.IntegerField(default=2000)

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return self.name


class Viaje(models.Model):
    STATUS = ((0, "Bueno"), (1, "Regular"), (2, "Malo"))
    id = models.Autofield(primary_key=True)
    viajero = models.ForeignKey(User, on_delete=models.CASCADE)
    conductor = models.ForeignKey(User, on_delete=models.CASCADE)
    destino = models.CharField(max_length=255)
    precio = models.IntegerField(default=0)
    puntuacion = models.IntegerFIeld(default=0, choices=STATUS)

    class Meta:
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"

    def __str__(self):
        return self.id

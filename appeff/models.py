from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conductor(models.Model):
    STATUS = ((0, "Disponible"), (1, "No disponible"))
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilidad = models.IntegerField(default=0, choices=STATUS)
    puntuacion = models.FloatField(default=0, choices=STATUS)


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=30)
    placa = models.CharField(max_length=10)
    anno = models.IntegerField(default=2000)

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return f"Auto de {self.user}"


class Viaje(models.Model):
    STATUS = ((1, "Malo"), (2, "Regular"), (3, "Neutro"), (4, "Bueno"), (5, "Excelente"))
    DISTRITOS = (("LIMA_CERCADO","LIMA CERCADO"),("ATE","ATE"),("BARRANCO","BARRANCO"),("LINCE","LINCE"),("MIRAFLORES","MIRAFLORES"))
    id = models.AutoField(primary_key=True)
    viajero = models.ForeignKey(User, on_delete=models.CASCADE)
    conductor = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    distrito = models.CharField(choices=STATUS)
    destino = models.CharField(max_length=255)
    precio = models.IntegerField(default=0)
    puntuacion = models.IntegerField(null=True, blank=True, choices=STATUS)

    class Meta:
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"

    def __str__(self):
        return self.id

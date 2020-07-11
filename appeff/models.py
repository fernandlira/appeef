from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conductor(models.Model):
    STATUS = ((0, "Disponible"), (1, "No disponible"))
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    disponibilidad = models.IntegerField(default=0, choices=STATUS)
    puntuacion = models.FloatField(default=0)

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"

    def __str__(self):
        return self.user.username


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
    PUNTOS = ((1, "Malo"), (2, "Regular"), (3, "Neutro"), (4, "Bueno"), (5, "Excelente"))
    DISTRITOS = (("LIMA_CERCADO","LIMA CERCADO"),("ATE","ATE"),("BARRANCO","BARRANCO"),("LINCE","LINCE"),("MIRAFLORES","MIRAFLORES"))
    id = models.AutoField(primary_key=True)
    viajero = models.ForeignKey(User, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor, blank=True, null=True, on_delete=models.CASCADE)
    distrito = models.CharField(max_length=60,choices=DISTRITOS,blank=False, null=False)
    destino = models.CharField(max_length=255,blank=False, null=False)
    precio = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    puntuacion = models.IntegerField(null=True, blank=True, choices=PUNTOS)

    class Meta:
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"

    def __str__(self):
        return str(self.id)

class Favorito(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    distrito = models.CharField(max_length=60, blank=False, null=False)
    destino = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return self.destino

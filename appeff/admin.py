from django.contrib import admin
from .models import Viaje, Auto, Conductor

# Register your models here.
class AutoAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "modelo"]


class ViajeAdmin(admin.ModelAdmin):
    list_display = ["id", "viajero", "conductor", "destino", "precio", "puntuacion"]


class ConductorAdmin(admin.ModelAdmin):
    list_display = ["id", "disponibilidad"]


admin.site.register(Auto, AutoAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Conductor, ConductorAdmin)

from django import forms
from .models import Viaje, Conductor

class ViajeForm(forms.Form):
    DISTRITOS = (("LIMA_CERCADO","LIMA CERCADO"),("ATE","ATE"),("BARRANCO","BARRANCO"),("LINCE","LINCE"),("MIRAFLORES","MIRAFLORES"))
    conductor = forms.ModelChoiceField(queryset=Conductor.objects.filter(disponibilidad=int(0)), required=True)
    distrito = forms.ChoiceField(choices=DISTRITOS, required=True)
    destino = forms.CharField(required=True)
    
    #conductor.widget.attrs.update({'class': 'form-control'})
    distrito.widget.attrs.update({'class': 'form-control'})
    destino.widget.attrs.update({'class': 'form-control'})

class AceptarForm(forms.Form):
    precio = forms.FloatField(required=True)

    #conductor.widget.attrs.update({'class': 'form-control'})
    precio.widget.attrs.update({'class': 'form-control'})

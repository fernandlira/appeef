from django import forms
from .models import Viaje, Conductor

class ViajeForm(forms.Form):
    DISTRITOS = (("LIMA_CERCADO","LIMA CERCADO"),("ATE","ATE"),("BARRANCO","BARRANCO"),("LINCE","LINCE"),("MIRAFLORES","MIRAFLORES"))
<<<<<<< HEAD
    #conductor = forms.ModelChoiceField(queryset=Conductor.objects.filter(disponibilidad=0), required=True)
=======
    conductor = forms.ModelChoiceField(queryset=Conductor.objects.filter(disponibilidad=int(0)), required=True)
>>>>>>> 38a1004c94b52f9557ba490b6f2594a2a325f1c6
    distrito = forms.ChoiceField(choices=DISTRITOS, required=True)
    destino = forms.CharField(required=True)
    
    #conductor.widget.attrs.update({'class': 'form-control'})
    distrito.widget.attrs.update({'class': 'form-control'})
    destino.widget.attrs.update({'class': 'form-control'})

class AceptarForm(forms.Form):
    precio = forms.FloatField(required=True)

    #conductor.widget.attrs.update({'class': 'form-control'})
    precio.widget.attrs.update({'class': 'form-control'})
from django import forms
from django.forms.widgets import DateInput
from applications.crudModelos.models import Reserva

class ReservaForm(forms.ModelForm):
    check_in=forms.DateField(
        widget=DateInput(attrs={
            'class':'form-control'
        })
    )
    check_out=forms.DateField(
        widget=DateInput(attrs={
            'class':'form-control'
        })
    )
    class Meta:
        model=Reserva
        fields=['check_in','check_out']
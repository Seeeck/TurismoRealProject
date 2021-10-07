import datetime
from datetime import date
from django import forms
from django.forms.widgets import DateInput
from applications.crudModelos.models import Reserva

class DateInput(forms.DateInput):
    input_type='date'

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

    def clean_check_in(self):
        
        if(self.cleaned_data['check_in']<date.today()):
            
            raise forms.ValidationError('La fecha del llegada debe ser mayor a la actual')
            
        else:
            pass

    def clean_check_out(self):
        try:
            if(self.cleaned_data['check_in']):
                if(self.cleaned_data['check_out']<self.cleaned_data['check_in']):
                
                    raise forms.ValidationError('La fecha de vuelta es menor a la de Ida')
                else:
                    pass
        except:
            pass
        
        
        
        

import datetime
from datetime import date
from django import forms
from django.db.models import fields
from django.forms.widgets import DateInput
from applications.crudModelos.models import Reserva, Transporte
from applications.funcionario.views import Checkin

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
        print(date.today())
        checkin=self.cleaned_data['check_in']
        if(checkin<date.today()):
            
            raise forms.ValidationError('La fecha del llegada debe ser mayor a la actual')
        
        return checkin
            

    def clean_check_out(self):
        
        checkout=self.cleaned_data['check_out'] 
    
        if(checkout<self.cleaned_data['check_in']):
                
            raise forms.ValidationError('La fecha de vuelta es menor a la de Ida')
            
        return checkout
        
class InvalidForm(forms.ModelForm):
    class Meta:
        model=Reserva
        fields=[]       
        
        

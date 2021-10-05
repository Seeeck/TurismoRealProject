import datetime
from django import forms
from django.forms.widgets import DateInput
from itertools import cycle
from django.contrib.auth import authenticate,login, logout

from .models import User,Cliente
from rut_chile import rut_chile
from datetime import time

class DateInput(forms.DateInput):
    input_type='date'

class UserClienteRegisterForm(forms.ModelForm):
    
    email=forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese su correo',
                'class':'form-control'
            }
        )
    )

    rut_cliente=forms.CharField(
        label='Rut',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese su rut',
                'class':'form-control'
            }
        )
    )

    nombre_cliente=forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese su nombre',
                'class':'form-control'
            }
        )
    )

    apellido_cliente=forms.CharField(
        label='Apellido ',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingrese su apellido ',
                'class':'form-control'
            }
        )
    )

    fecha_nacimiento=forms.DateField(
        widget=DateInput(attrs={
            'class':'form-control'
        })
   
    )
 
    password1=forms.CharField(
        label='Clave',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Ingrese su nueva clave',
                'class':'form-control'
            }
        )
    )

    password2=forms.CharField(
        label='Clave',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir la Clave',
                'class':'form-control'
            }
        )
    )

#Configuracion del form heredado de modelo User
    class Meta:
        model=User
        fields=('email',)


    def clean_nombre_cliente(self):
        if len(str(self.cleaned_data['nombre_cliente']))<3:
            raise forms.ValidationError('El nombre debe ser mayor a 2 caracteres')
        return self.cleaned_data['nombre_cliente']
    
    def clean_apellido_cliente(self):
        if len(str(self.cleaned_data['apellido_cliente']))<3:
            raise forms.ValidationError('El apellido debe ser mayor a 2 caracteres')
        return self.cleaned_data['apellido_cliente']
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Las claves deben coincidir')
        return self.cleaned_data['password2']
    
    def clean_rut_cliente(self):
        if rut_chile.is_valid_rut(str(self.cleaned_data['rut_cliente'])):
            return self.cleaned_data['rut_cliente']
        else:
            raise forms.ValidationError('Rut invalido')
        
    def clean_fecha_nacimiento(self):
        print(int(datetime.date.today().year)-(int(self.cleaned_data['fecha_nacimiento'].year)))
        if int(datetime.date.today().year)-(int(self.cleaned_data['fecha_nacimiento'].year))>=18 :
            return self.cleaned_data['fecha_nacimiento']
        else:
            raise forms.ValidationError('Debe ser mayor de edad')

            

     

class LoginForm(forms.Form):
    email=forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Email',
                'class':'form-control'
            }
        )
    )

    password=forms.CharField(
        label='Clave',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Clave',
                'class':'form-control'
            }
        )
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        # do your custom validations / transformations here
        # and some more
        return cleaned_data 

    def clean_email(self):
        try:
            
            user=User.objects.get(email=self.cleaned_data.get('email'))
            return self.cleaned_data.get('email')
        except:
            raise forms.ValidationError('No existe el email en el sistema')
    
    def clean_password(self):
        if(len(self.cleaned_data['password'])<2):
            raise forms.ValidationError('Ingrese una clave valida')
        auth=authenticate(
            username=str(self.clean_email()),
            password=self.cleaned_data['password'] 
            )
        
        if auth:
            return self.cleaned_data['password']
        else:
            raise forms.ValidationError('La clave es incorrecta')

            

    
    
        



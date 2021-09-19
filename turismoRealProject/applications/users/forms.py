from django import forms
from django.forms.widgets import DateInput

from .models import User,Cliente


class DateInput(forms.DateInput):
    input_type='date'

class UserClienteRegisterForm(forms.ModelForm):
    
    email=forms.CharField(
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
        widget=DateInput
   
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

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las claves no son iguales')


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



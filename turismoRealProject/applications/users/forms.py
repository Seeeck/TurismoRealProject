from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(
        label='Clave',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Clave'
            }
        )
    )

    password2=forms.CharField(
        label='Clave',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Clave'
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
                'placeholder':'Email'
            }
        )
    )

    password=forms.CharField(
        label='Clave',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Clave'
            }
        )
    )
   
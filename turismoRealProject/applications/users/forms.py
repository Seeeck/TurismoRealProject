from django import forms

from .models import User

class UserRegisterForm(forms.ModelForm):


#Configuracion del form heredado de modelo User
    class Meta:
        model=User
        fields=('__all__')
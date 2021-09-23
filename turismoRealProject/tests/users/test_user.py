#importamos pytest 
from django.db.models.fields import NullBooleanField
import pytest

#importamos el user del modelo
from applications.users.models import User

#se define el nombre de la función
#EN este caso será la creación del usuario
#Para dar acceso a la BD:
@pytest.mark.django_bd
def  test_user_creation():
    user = User.objects.create_user(
        email='kevin@gmail.com',
        username=''
    )
    #assert: para comprobar si la condición es verdad o no lo es
    assert user.email == 'kevin@gmail.com'
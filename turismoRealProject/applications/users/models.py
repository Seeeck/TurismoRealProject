from django.db import models

# Create your models here.
#auth viene de la aplicacion auth
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.db.models.fields import CharField
from .managers import UserManager
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=40,unique=True)
    #
    first_name = models.CharField( max_length=50,null=True)
    last_name = models.CharField( max_length=50,null=True)
    is_active = models.BooleanField(default=True)
    username = models.CharField( max_length=50,null=True)
    is_staff = models.BooleanField(default=False)
    is_funcionario=models.BooleanField(default=False)
#se aplica aca el email como username
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    #Se usa el manager de userManager
    objects=UserManager()
    def get_email(self):
        return self.email
    class Meta:
        verbose_name='Usuario'

class Cliente(models.Model):
    rut=models.CharField(max_length=20,primary_key=True,unique=True)
    nombre=models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    user_cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "rut:"+self.rut+" nombre:"+self.nombre+" "+self.apellido
    class Meta:
        verbose_name='Cliente'

from django.db import models
from django.contrib.auth.hashers import make_password
#necesitamos redefinir como se crean los usuarios
#no puedo crear un superuser sin esto
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager,models.Manager):

    #Se especifica que obligatoriamente necesitamos un email
    def _create_user(self,email,password,is_staff,is_superuser,**extra_fields):
        user=self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    #Para que no sea un staff false y no super usuario false
    def create_user(self,email,password=None,**extra_fields):
        return self._create_user(email,password,False,False,**extra_fields)
#Esto es de administrador
    def create_superuser(self,email,password=None,**extra_fields):
        return self._create_user(email,password,True,True,**extra_fields)
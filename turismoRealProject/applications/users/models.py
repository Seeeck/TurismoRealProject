from django.db import models

# Create your models here.
#auth viene de la aplicacion auth
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    #
    is_staff = models.BooleanField(default=False)
#se aplica aca el email como username
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    #Se usa el manager de userManager
    objects=UserManager()
     
    def get_email(self):
        return self.email
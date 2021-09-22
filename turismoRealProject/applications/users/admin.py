from django.contrib import admin
from django.db import models
from django import forms
from django.db.models import fields
from .models import User,Cliente
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.admin import UserAdmin
# Register your models here.



admin.site.register(Cliente)


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','is_funcionario','is_superuser' )


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {}
    fieldsets = (
        (None, {'fields': ('password',)}),
        (('Personal info'), {'fields': (  'email',)}),
        (('Permissions'), {
            'fields': ('is_superuser','is_funcionario'  ),
        }),
        (('Important dates'), {'fields': ( )}),
    )
    add_fieldsets = (
        (None, {
            
            'fields': ( 'email','password1', 'password2', 'is_funcionario','is_superuser'),
        }),     
    )
    list_display=(
        'email',
        'password',
    )
    
   
    
admin.site.register(User,UserAdmin)


from django.forms.forms import Form
from django.shortcuts import render
from django.urls import reverse_lazy,reverse

from .forms import UserRegisterForm,LoginForm
from .models import User
from django.views.generic.edit import(FormView)
from django.views.generic import(CreateView,View)
#para la autenticacion
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect

class UserRegisterView(FormView):
    template_name='users/cliente/register.html'

    form_class=UserRegisterForm
    success_url='/'

    def form_valid(self,form):
        #Recupero los valores del formulario que esta en el template del propio form
        #para insertarlos en la funcion de createuser
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            #se pueden agregar otros atributos extras del model que no correspondan 
            #a los valores por defecto de la funcion create_user
        )
        return super(UserRegisterView,self).form_valid(form)


class LoginUser(FormView):
    template_name='users/cliente/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('home_app:inicio')

    def form_valid(self,form):
        #verificacion con authenticate
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        #Con esto se realiza el login y el propio request
        login(self.request,user)
        return super(LoginUser,self).form_valid(form)

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        #funcion para cerrar la sesion actua;
        logout(request)
        return HttpResponseRedirect(
            #reverse sirve para navegar por las url del sistema para buscar una
            reverse(
                'users_app:user-login'
            )
        )
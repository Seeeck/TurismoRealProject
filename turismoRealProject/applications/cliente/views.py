

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import(TemplateView)


class Inicio(TemplateView):
    template_name="sistemaCliente/inicio.html"
    

class InicioCliente(LoginRequiredMixin,TemplateView):
    template_name = "sistemaCliente/panel_usuario.html"
    login_url=reverse_lazy('users_app:user-login')


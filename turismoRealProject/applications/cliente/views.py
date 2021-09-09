

# Create your views here.
from django.shortcuts import render

from django.views.generic import(TemplateView)


class InicioCliente(TemplateView):
    template_name = "cliente/index.html"

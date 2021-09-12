from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
# Create your views here.


class FuncionarioPanelPrincialView(LoginRequiredMixin,TemplateView):
    template_name = "sistemaFuncionario/index.html"
    login_url=reverse_lazy('users_app:userFuncionario-login')

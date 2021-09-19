from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
# Create your views here.


class FuncionarioPanelPrincialView(LoginRequiredMixin,TemplateView):
    template_name = "sistemaFuncionario/index.html"
    login_url=reverse_lazy('users_app:userFuncionario-login')
    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_funcionario==False:
            return redirect('cliente_app:inicio-principal')
        return super(FuncionarioPanelPrincialView,self).dispatch(request,*args,**kwargs)

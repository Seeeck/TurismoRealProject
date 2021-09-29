

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import(TemplateView)
from django.views.generic import CreateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from applications.users.models import User
from django.views.generic  import ListView
#Modelos
from applications.crudModelos.models import Departamento
# Create your views here.

from django.http import request



class Inicio(TemplateView):
    template_name="sistemaCliente/inicio.html"
    

class ListaDepartamentos(LoginRequiredMixin,ListView):
    
    template_name = "sistemaCliente/inicio_cliente.html"
    login_url=reverse_lazy('users_app:user-login') 
    paginate_by=4
    model=Departamento
    context_object_name = "departamentos"

    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_funcionario:
            return redirect('funcionario_app:panel-funcionario')
        return super(ListaDepartamentos,self).dispatch(request,*args,**kwargs)


        
    



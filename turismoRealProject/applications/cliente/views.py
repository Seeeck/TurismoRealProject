
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import(TemplateView,CreateView)
from django.views.generic  import ListView
#Modelos
from applications.crudModelos.models import Departamento,Reserva
#Forms
from .forms import ReservaForm
# Create your views here.
from django.http import HttpRequest






class Inicio(TemplateView):
    template_name="sistemaCliente/inicio.html"
    

class ListaDepartamentosView(LoginRequiredMixin,ListView):
    
    template_name = "sistemaCliente/lista_departamentos.html"
    login_url=reverse_lazy('users_app:user-login') 
    paginate_by=4
    model=Departamento
    context_object_name = "departamentos"

    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_funcionario:
            return redirect('funcionario_app:panel-funcionario')
        return super(ListaDepartamentosView,self).dispatch(request,*args,**kwargs)
    
    def get_queryset(self):
        comuna=self.request.GET.get("comuna","")
        
        lista=Departamento.objects.filter(id_zona__comuna__icontains=comuna)

        return lista
        
        
class ReservarDepartamentoView(LoginRequiredMixin,CreateView):
    model=Reserva
    template_name="sistemaCliente/realizar_reserva.html"
    form_class=ReservaForm
    context_object_name='departamento'
    

    def get_context_data(self,**kwargs):
        context = super(ReservarDepartamentoView, self).get_context_data(**kwargs)
        departamento=Departamento.objects.get(id_departamento=self.kwargs['id_departamento'])
        context['imagen_departamento']=departamento.imagen_departamento
        context['nombre_departamento']=departamento.nombre_departamento
        context['numero_personas']=departamento.numero_personas
        context['lista_personas']=range(1,departamento.numero_personas)
        context['valor_dia']=departamento.valor_dia
        context['valor_anticipo']=departamento.valor_anticipo
        return context

    def form_valid(self,form):
        print("a@@@@@@@@@")
        print(self.request.POST.get('nombre0'))
        print(self.request.POST.get('nombre1'))

        return super(ReservarDepartamentoView,self).form_valid(form)
    
    

    
    
    
    
 
    


    
    




        
    




from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import(TemplateView,CreateView)
from django.views.generic  import ListView
from django.contrib.messages.views import SuccessMessageMixin
#Modelos
from applications.crudModelos.models import Departamento,Reserva
from applications.crudModelos.models import Sv_Tour,Sv_Transporte,CheckIn,CheckOut,Transporte
from applications.users.models import Cliente


#Forms
from .forms import ReservaForm
# Create your views here.
from django.http import HttpRequest



def cliente_full_name(cliente):
    cliente_nombre=cliente.nombre
    cliente_apellido=cliente.apellido
    cliente_full_name=cliente_nombre+' '+cliente_apellido
    return cliente_full_name


class Inicio(TemplateView):
    template_name="sistemaCliente/inicio.html"


    def get_context_data(self,**kwargs):
        if(str(self.request.user)=='AnonymousUser'):
            pass
        else:
            context = super(TemplateView, self).get_context_data(**kwargs)
            cliente=Cliente.objects.get(user_cliente=self.request.user)
            context['nombre_cliente']=cliente_full_name(cliente) 
            return context
    

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
        
        lista=Departamento.objects.filter(id_zona__comuna__icontains=comuna,estado_departamento=True)
        

        return lista
    def get_context_data(self,**kwargs):
        context = super(ListaDepartamentosView, self).get_context_data(**kwargs)
        cliente=Cliente.objects.get(user_cliente=self.request.user)
        
        context['nombre_cliente']=cliente_full_name(cliente)
        return context
        
        
class ReservarDepartamentoView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model=Reserva
    template_name="sistemaCliente/realizar_reserva.html"
    form_class=ReservaForm
    context_object_name='departamento'
    success_url=reverse_lazy('cliente_app:lista_departamentos')
    success_message='Reserva realizada'
    def get_context_data(self,**kwargs):
        context = super(ReservarDepartamentoView, self).get_context_data(**kwargs)
        cliente=Cliente.objects.get(user_cliente=self.request.user)
        departamento=Departamento.objects.get(id_departamento=self.kwargs['id_departamento'])
        tour=Sv_Tour.objects.get(id_tour=departamento.id_tour.id_tour)
        sv_transporte=Sv_Transporte.objects.get(id_sv_transporte=departamento.id_sv_transporte.id_sv_transporte)
        context['imagen_departamento']=departamento.imagen_departamento
        context['nombre_departamento']=departamento.nombre_departamento
        context['numero_personas']=departamento.numero_personas
        context['lista_personas']=range(1,departamento.numero_personas)
        context['valor_dia']=departamento.valor_dia
        context['valor_anticipo']=departamento.valor_anticipo
        context['is_tour']=departamento.is_tour
        context['is_transporte']=departamento.is_transporte
        context['valor_tour']=tour.valor_tour
        context['valor_sv_transporte']=sv_transporte.valor_transporte
        context['direccion_departamento']=departamento.direccion_departamento
        context['nombre_cliente']=cliente_full_name(cliente)
        return context

    def form_valid(self,form):

        
        reserva=form.save()
        checkin=CheckIn.objects.create(fecha_checkin=self.request.POST.get('check_in'))
        checkout=CheckOut.objects.create(fecha_checkout=self.request.POST.get('check_out'))
        sv_transporte=Sv_Transporte.objects.filter(sv_transporte_disponible=True).first()
        transporte=Transporte.objects.create(fecha_ida=self.request.POST.get('check_in'),
                                             fecha_vuelta=self.request.POST.get('check_out'),
                                             direccion_inicio=self.request.POST.get('direccionInicioTransporte')
                                             ,id_sv_transporte=sv_transporte)
        departamento=Departamento.objects.get(id_departamento=self.kwargs['id_departamento'])
        departamento.estado_departamento=False
        departamento.save()
        cliente=Cliente.objects.get(user_cliente=self.request.user.id )
        reserva.is_pago_anticipo=True
        reserva.id_departamento=departamento
        reserva.id_cliente=cliente
        reserva.id_check_in=checkin
        reserva.id_check_out=checkout
        reserva.id_transporte=transporte
        reserva.save()
        
        return super(ReservarDepartamentoView,self).form_valid(form)
    
    

    
    
    
    
 
    


    
    




        
    



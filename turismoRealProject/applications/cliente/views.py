
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.views.generic import(TemplateView,CreateView)
from django.views.generic  import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
#Modelos
from applications.crudModelos.models import Departamento,Reserva
from applications.crudModelos.models import Sv_Tour,Sv_Transporte,CheckIn,CheckOut,Transporte,PersonaExtra
from applications.users.models import Cliente

#Datetime
from datetime import date, datetime
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
        try:
            if(str(self.request.user)=='AnonymousUser'):
                pass
            else:
                context = super(TemplateView, self).get_context_data(**kwargs)
                cliente=Cliente.objects.get(user_cliente=self.request.user)
                context['nombre_cliente']=cliente_full_name(cliente) 
                return context
        except:
            pass
    

class ListaDepartamentosView(LoginRequiredMixin,ListView):
    
    template_name = "sistemaCliente/lista_departamentos.html"
    login_url=reverse_lazy('users_app:user-login') 
    paginate_by=4
    model=Departamento
    context_object_name = "departamentos"

    def dispatch(self,request,*args,**kwargs):
        try:
            if self.request.user.is_funcionario:
                return redirect('funcionario_app:panel-funcionario')
        except:
            pass
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

        departamento=Departamento.objects.get(id_departamento=self.kwargs['id_departamento'])
        departamento.estado_departamento=False
        departamento.save()

        cliente=Cliente.objects.get(user_cliente=self.request.user.id )

        reserva.is_pago_anticipo=True
        reserva.id_departamento=departamento
        reserva.id_cliente=cliente
        reserva.id_check_in=checkin
        reserva.id_check_out=checkout 

        nombre_persona=''
        apellido_persona=''
        cantidad_personas=0
        for key,value in self.request.POST.items():
            if (str(key).__contains__('nombre') or str(key).__contains__('apellido')) and str(value)!=''   :
                if(str(key).__contains__('nombre')):
                    nombre_persona=value
                    p=PersonaExtra.objects.create(nombre=nombre_persona,id_reserva=reserva)
                    id=p.id_persona_extra
                    
                elif(str(key).__contains__('apellido')):  
                    apellido_persona=value
                    p2=PersonaExtra.objects.get(id_persona_extra=id)
                    p2.apellido=apellido_persona
                    cantidad_personas=cantidad_personas+1
                    p2.save()
        precio_tour=0
        if(self.request.POST.get('tourCheck')=='true'):
            reserva.is_tour=True
            precio_tour=(departamento.id_tour.valor_tour)*cantidad_personas
        precio_transporte=0
        if(self.request.POST.get('transporteCheck')=='true'):
            reserva.is_transporte=True
            precio_transporte=(departamento.id_sv_transporte.valor_transporte)*cantidad_personas
            sv_transporte=Sv_Transporte.objects.filter(sv_transporte_disponible=True).first()
            transporte=Transporte.objects.create(fecha_ida=self.request.POST.get('check_in'),
                                             fecha_vuelta=self.request.POST.get('check_out'),
                                             direccion_inicio=self.request.POST.get('direccionInicioTransporte')
                                             ,id_sv_transporte=sv_transporte)
            reserva.id_transporte=transporte

        
        dias=((datetime.strptime(reserva.id_check_out.fecha_checkout,'%Y-%m-%d'))-(datetime.strptime(reserva.id_check_in.fecha_checkin,'%Y-%m-%d'))).days
        precio_departamento_dias=departamento.valor_dia*dia
        valor_total=precio_departamento_dias+precio_tour+precio_transporte

        reserva.valor_total=valor_total
        reserva.save()
        return super(ReservarDepartamentoView,self).form_valid(form)


class ListaReservasView(LoginRequiredMixin,ListView):
    template_name = "sistemaCliente/lista_reservas.html"
    model = Reserva
    context_object_name='reservas'
    
    def get_queryset(self):   
        cliente=Cliente.objects.get(user_cliente=self.request.user)
        reservas=Reserva.objects.filter(id_cliente=cliente)
        
        return reservas

    def get_context_data(self,**kwargs):
        context = super(ListaReservasView, self).get_context_data(**kwargs)
        cliente=Cliente.objects.get(user_cliente=self.request.user)
        
        context['nombre_cliente']=cliente_full_name(cliente)
        return context
    
 
    


    
    




        
    



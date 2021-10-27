from typing import Any
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView , ListView , View , DetailView
from django.shortcuts import redirect, render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from applications.funcionario.models import Item 


from applications.users.models import Cliente, User
from applications.crudModelos.models import Reserva

# Create your views here.


class FuncionarioPanelPrincialView(LoginRequiredMixin,TemplateView):
    template_name = "sistemaFuncionario/index.html"
    login_url=reverse_lazy('users_app:userFuncionario-login')
    def dispatch(self,request,*args,**kwargs):
        if self.request.user.is_funcionario==False:
            return redirect('cliente_app:inicio-principal')
        return super(FuncionarioPanelPrincialView,self).dispatch(request,*args,**kwargs)


class Checkin(TemplateView):    
    template_name = 'sistemaFuncionario/checkin.html' 
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        
        if query :

            try:
            
                context['cliente'] = Cliente.objects.get(
       
                Q(rut=query) | Q(nombre=query))
            
            except ObjectDoesNotExist:
                
                print('dsds')

           
            context['Reservas'] = Reserva.objects.filter(id_cliente=context['cliente'].rut )
        
        return context


class ListadoClientes(ListView):
    
    model  =  Cliente
    context_object_name = 'listado_clientes'
    # queryset = Cliente.objects.filter(title__icontains='war')
    template_name = 'sistemaFuncionario/listado_clientes.html' 
    def get_queryset(self):
        object_list = Cliente.objects.all()
        query = self.request.GET.get('q')
        
        if query :
            object_list = Cliente.objects.filter(
                Q(rut__icontains=query) | Q(nombre__icontains=query))

        return object_list


class ListadoItem(ListView):
    
    model  =  Item
    context_object_name = 'items'
    template_name = 'sistemaFuncionario/listado_items.html' 
    
    def get_queryset(self):
        

        id = self.kwargs['pk']   
        return Item.objects.filter(id_departamento=id)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['select'] = forms.ChoiceField(widget=forms.Select, choices=ESTADO_CHOICES)
    #     return context
    

class DetalleCliente(DetailView):

    model = Cliente
    template_name = 'sistemaFuncionario/detalle_cliente.html' 

    def get_context_data(self, **kwargs):
        

        context = super().get_context_data(**kwargs)
        try:
            id = self.kwargs['pk']
            print(id)   
            context['Reservas'] = Reserva.objects.filter(id_cliente=id)
        except ObjectDoesNotExist:
            context['Mensaje'] = 'No tiene reservas'
        except:
            context['Mensaje'] = '.....ERROR...'
        # print(reserva)
        
        return context
    

def modificar_estado(request):
    ids = request.POST.getlist('id_item')
    items= Item.objects.filter(id__in=ids)
    items_modificado=[]
    estados = request.POST.getlist('opciones')
    for index,item in enumerate(items):
        item.estado = estados[index]
        items_modificado.append(item)
    
    Item.objects.bulk_update(items_modificado,['estado'])

    
    return HttpResponseRedirect(reverse('funcionario_app:listadoItem',kwargs={'pk':items[0].id_departamento.id_departamento}))

from django.conf import settings
from django.core.mail import EmailMultiAlternatives, message
from django.template.loader import get_template
def send_user_mail(request,id):
    
    cliente = Cliente.objects.get(rut=id)
    subject = 'Terminos y condicciones'
    template = get_template('sistemaFuncionario/template_correo.html')

    content = template.render({
        'nombre': cliente.nombre,
        'apellido': cliente.apellido,
       


    })

    message = EmailMultiAlternatives(subject,
                                    '',settings.EMAIL_HOST_USER,
                                    [cliente.user_cliente.email]) 

    message.attach_alternative(content, 'text/html')
    message.send()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    
   
from django.forms.forms import Form
from django.shortcuts import render
from django.urls import reverse_lazy,reverse


from .models import User,Cliente
#importacion de vistas
from .forms import LoginForm, UserClienteRegisterForm
from django.views.generic.edit import(FormView)
from django.views.generic import(CreateView,View)
#para la autenticacion
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect


######Cliente########
class UserClienteRegisterView(FormView):
    template_name='users/cliente/registro.html'

    form_class=UserClienteRegisterForm
    
    success_url=reverse_lazy('cliente_app:inicio-principal')
    def form_valid(self,form):
        #Recupero los valores del formulario que esta en el template del propio form
        #para insertarlos en la funcion de createuser

        user=User(
            email=form.cleaned_data['email'],
            is_staff=False,
            is_superuser=False
            )
        user.set_password(form.cleaned_data['password1'])
        user.save()
        # User.objects.create_user(
        #     user.email,
        #     user.password,
        # )

        rut=form.cleaned_data['rut_cliente']
        nombre=form.cleaned_data['nombre_cliente']
        apellido=form.cleaned_data['apellido_cliente']
        fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
  
        Cliente.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            user_cliente=user
        )

        

        return super(UserClienteRegisterView,self).form_valid(form)


class LoginUser(FormView):
    template_name='users/cliente/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('cliente_app:inicio-cliente')

    def form_valid(self,form):
        #verificacion con authenticate
        user_object= User.objects.get(email=form.cleaned_data['email'])
        if user_object.is_funcionario==False:
            user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password'] 
            )
            login(self.request,user)
        
        print('######desdeLoginUser!!!!!!!!')
        #Con esto se realiza el login y el propio request
        
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

class LoginAdmin(FormView):
    template_name='users/admin/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('admin:index')
    
    def form_valid(self,form):
        #verificacion con authenticate
        print('#########desde view logindmin')
        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        print(user)
        
        #Con esto se realiza el login y el propio request
        login(self.request,user)
        return super(LoginAdmin,self).form_valid(form)

        


class LoginFuncionario(FormView):
    template_name='users/funcionario/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('funcionario_app:panel-funcionario')
    
    def form_valid(self,form):
        #verificacion con authenticate
        user_object= User.objects.get(email=form.cleaned_data['email'])
        print('#######Desde Login Funcionario #########')
        if user_object.is_funcionario:
            user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password']
            )
        

        
        #Con esto se realiza el login y el propio request
        login(self.request,user)
        return super(LoginFuncionario,self).form_valid(form)

class LogoutFuncionarioView(View):
    def get(self,request,*args,**kwargs):
        #funcion para cerrar la sesion actua;
        logout(request)
        return HttpResponseRedirect(
            #reverse sirve para navegar por las url del sistema para buscar una
            reverse(
                'users_app:userFuncionario-login'
            )
        )
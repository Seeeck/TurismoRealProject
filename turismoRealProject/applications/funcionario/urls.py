
from django.urls import path
from . import views

app_name="funcionario_app"
urlpatterns = [
    #Clientes
    path('/panel-Funcionario', views.FuncionarioPanelPrincialView.as_view(),name='panel-funcionario'),
    path('/listadoCliente', views.ListadoClientes.as_view(),name='listadoCliente'),
    path('/listadoItem/<slug:pk>', views.ListadoItem.as_view(),name='listadoItem'),
     path('/detalleCliente/<pk>', views.DetalleCliente.as_view(), name='cliente-detalle'),
     path('/modificarEstado', views.modificar_estado, name='modificar-estado'),
     path('/checkin', views.Checkin.as_view(), name='checkin'),
     path('/enviarCorrreo/<int:id>', views.send_user_mail, name='enviar-correo'),



    


]


from django.urls import path
from . import views

app_name="funcionario_app"
urlpatterns = [
    #Clientes
    path('panel-Funcionario', views.FuncionarioPanelPrincialView.as_view(),name='panel-funcionario'),
 


]

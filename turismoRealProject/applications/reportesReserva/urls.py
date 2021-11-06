
from django.urls import path
from . import views

app_name="reportes_app"
urlpatterns = [
    #Clientes
    path('/panel-Funcionario', views.FuncionarioPanelPrincialView.as_view(),name='panel-funcionario'),
]

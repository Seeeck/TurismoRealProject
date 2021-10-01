
from django.urls import path
from . import views

app_name="cliente_app"
urlpatterns = [
    path('',views.Inicio.as_view(),name='inicio-principal'),
    path('cliente/lista-departamentos/', views.ListaDepartamentosView.as_view(),name='lista_departamentos'),
    path('cliente/reserva-departamento/<id_departamento>', views.ReservarDepartamentoView.as_view(),name='reservar-departamento'),


]


from django.urls import path
from . import views

app_name="cliente_app"
urlpatterns = [
    path('',views.Inicio.as_view(),name='inicio-principal'),
    path('cliente/lista-departamentos/', views.ListaDepartamentosView.as_view(),name='lista_departamentos'),
    path('cliente/reserva-departamento/<id_departamento>', views.ReservarDepartamentoView.as_view(),name='reservar-departamento'),
    path('cliente/reservas/',views.ListaReservasView.as_view(),name='lista-reservas'),
    path('cliente/reservas/<id_reserva>',views.EditarReservaView.as_view(),name='editar-reserva'),

    


]

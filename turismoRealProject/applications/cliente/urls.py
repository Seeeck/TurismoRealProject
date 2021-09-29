
from django.urls import path
from . import views

app_name="cliente_app"
urlpatterns = [
    path('',views.Inicio.as_view(),name='inicio-principal'),
    path('cliente/lista-departamentos/', views.ListaDepartamentos.as_view(),name='lista_departamentos'),

]

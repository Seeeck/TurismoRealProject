
from django.urls import path
from . import views

app_name="cliente_app"
urlpatterns = [
    path('',views.Inicio.as_view(),name='inicio-principal'),
    path('inicio-cliente/', views.InicioCliente.as_view(),name='inicio-cliente'),

]

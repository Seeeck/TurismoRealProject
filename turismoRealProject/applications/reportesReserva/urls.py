
from django.urls import path
from . import views

app_name="reportes_app"
urlpatterns = [
    #Clientes
    path('reportes', views.reportesView,name='reportes'),
]
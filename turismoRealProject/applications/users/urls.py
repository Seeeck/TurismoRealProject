
from django.urls import path
from . import views

app_name="users_app"
urlpatterns = [
    #Clientes
    path('registro/', views.UserClienteRegisterView.as_view(),name='user-register'),
    path('login/', views.LoginUser.as_view(),name='user-login'),
    path('logout/', views.LogoutView.as_view(),name='user-logout'),
    #administrador
    path('loginAdmin/', views.LoginAdmin.as_view(),name='userAdmin-login'),
    #funcionario
    path('loginFuncionario/', views.LoginFuncionario.as_view(),name='userFuncionario-login'),
    path('logoutFuncionario/', views.LogoutFuncionarioView.as_view(),name='userFuncionario-logout'),


]

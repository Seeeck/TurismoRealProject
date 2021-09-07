from django.urls import path
from . import views

app_name="home_app"
urlpatterns = [
    path('inicio/', views.HomePage.as_view(),name='inicio'),

]

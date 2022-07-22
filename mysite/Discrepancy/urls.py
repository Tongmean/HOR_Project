from django.urls import path
from . import views


urlpatterns = [
    #Home page
    #path('', views.Home, name='Home'),
    path('Home', views.Home, name='Home'),
    
    path('login', views.login, name='login'),
    
    #Shipmentform
    path('Shipmentform', views.Shipmentform, name='Shipmentform'),
    path('Addform', views.Addform, name='Addform'),
    path('AddformLay', views.AddformLay, name='AddformLay'),
    #Logicstic Decision
    
]
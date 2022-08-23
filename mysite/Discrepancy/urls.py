from django.urls import path
from . import views


urlpatterns = [
    path('genpdf/<int:pk>', views.genpdf , name='genpdf'),
    path('Example', views.Example, name='Example'),
    #Home page
    #path('', views.Home, name='Home'),
    path('Home', views.Home, name='Home'),
    
    path('login', views.login, name='login'),
    
    #Shipmentform
    path('Shipmentform', views.Shipmentform, name='Shipmentform'),
    path('Addform', views.Addform, name='Addform'),
    path('AddData/<int:pk>', views.AddData, name='AddData'),
    #Supervisor
    path('Action', views.Action_cause, name='Action'),
    path('Action_Shipmentform', views.Action_Shipmentform, name='Action_Shipmentform'),
    path('AddAction/<int:pk>', views.AddAction, name='AddAction'),
    #Dashboard
    path('Dashboard', views.Dash, name='Dashboard')
]

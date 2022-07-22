from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views her
#Home Page
def Home(request):
    return render(request,'Home/Home.html')
def login(request):
    return render(request,'Home/login.html')
#Shipment Form
def Shipmentform(request):
    return render(request,'Shipmentform/Shipmentform.html')
def Addform(request):        
    return render(request,'Shipmentform/Addform.html')
def AddformLay(request):        
    return render(request,'Shipmentform/s.html')


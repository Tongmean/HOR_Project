from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import shipmentdata
# Create your views her
def Example(request):
    return render(request,'Example.html')
#Home Page
def Home(request):
    return render(request,'Home/Home.html')
def login(request):
    return render(request,'Home/login.html')
#Shipment Form
def Shipmentform(request):
    return render(request,'Shipmentform/Shipmentform.html')
def Addform(request):
    form = shipmentdata
    if request.method=='POST':
        form = shipmentdata(request.POST)
        if form.is_valid():
            form.save()   
    return render(request,'Shipmentform/Addform.html',)
# def AddformLay(request):        
#     return render(request,'Shipmentform/s.html')
#Dashboard
def Dash(request):        
    return render(request,'Dashboard/Dashboard.html')


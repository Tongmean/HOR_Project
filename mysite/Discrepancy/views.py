from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import Action_, Actionform, shipmentrecord, update
from datetime import datetime, timedelta, date
from datetime import date
from django.contrib import messages
# Create pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Addform
from .models import TdAction, TdSupervisorData, TdArea, JdModeoftransportation, JdDamageuom, TdTypeofdiscrepancy,TdDiscrepancyrecordform
# Create your views here

def genpdf(request, pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)
    records = TdSupervisorData.objects.filter(cause_actionid = pk)
    lines = ["Discrepancy record Detail"]

    for record in records:
        lines.append("-------------------------------")
        
        lines.append("Action Record Detail")
        lines.append("")
        lines.append("ActionID          :  " + str(record.cause_actionid))
        lines.append("RootCause         :  " + str(record.rootcause))
        lines.append("Action            :  " + str(record.actionid.action))
        lines.append("Report Date       :  " + str(record.report_date))
        lines.append("Report By         :  " + str(record.report_by))
        lines.append("Processing Time   :  " + str(record.status))
        #----
        lines.append("")
        lines.append("Shipment Record List")
        lines.append("--------------------------")
        lines.append("")
        lines.append("Transaction_Number    :  "+str(record.transaction_number.transaction_number))
        lines.append("Area                  :  "+str(record.transaction_number.areaid.area))
        lines.append("Flight Number         :  "+str(record.transaction_number.fightnumber))
        lines.append("Mode of transportation:  "+str(record.transaction_number.modeoftransportationid.modeoftransportation))
        lines.append("Forwarder             :  "+str(record.transaction_number.forwarder))
        lines.append("Action                :  "+str(record.actionid.action))
        lines.append("Shipper Name          :  "+str(record.transaction_number.shippername))
        lines.append("Shipper Country       :  "+str(record.transaction_number.shippercountry))
        lines.append("Declaration Number    :  "+str(record.transaction_number.customs_declaration_number))
        lines.append("Invoice Number        :  "+str(record.transaction_number.invoice_number))
        lines.append("Pick Ticketor         :  "+str(record.transaction_number.pickticketor))
        lines.append("Bill of landing       :  "+str(record.transaction_number.mawb_hawb_bill_of_landing))
        lines.append("Supplier Name         :  "+str(record.transaction_number.suppliername))
        lines.append("Part Number           :  "+str(record.transaction_number.partnumber))
        lines.append("Invoice Quantity      :  "+str(record.transaction_number.invoice_quantity))
        lines.append("Invoice UOM           :  "+str(record.transaction_number.damageuomid.damageuom))
        lines.append("Unit Price            :  "+str(record.transaction_number.unitprice_field))
        lines.append("Total Package         :  "+str(record.transaction_number.total_package))
        lines.append("Date of Incident      :  "+str(record.transaction_number.dateofincident))
        lines.append("Type of Discrepancy   :  "+str(record.transaction_number.typeofdiscrepancyid.type_of_discrepancy))
        lines.append("Detail of Discrepancy :  "+str(record.transaction_number.detailofdiscrepancy))
        lines.append("Submit By             :  "+str(record.transaction_number.submitby))
        lines.append("Submit Date           :  "+str(record.transaction_number.submitdate))
        lines.append("Status                :  "+str(record.transaction_number.status))
        lines.append("-----------------------------------------    ")
  

    
    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename = 'Discrepancy Detail ' + str(pk))
    
def Example(request):
    return render(request,'Example.html')
#Home Page
def Home(request):
    today = datetime.today()
    my_date = date.today()
    this_month = datetime.now().month
    year, week_num, day_of_week = my_date.isocalendar()
    Today = TdSupervisorData.objects.filter(report_date=str(my_date)).count()
    week = TdSupervisorData.objects.filter(report_date__week=str(week_num)).count()
    month = TdSupervisorData.objects.filter(report_date__month=str(this_month)).count()
    year = TdSupervisorData.objects.filter(report_date__year=str(year)).count()
    all = TdSupervisorData.objects.all()
    short = TdSupervisorData.objects.filter(transaction_number__typeofdiscrepancyid = 2).count()
    Over = TdSupervisorData.objects.filter(transaction_number__typeofdiscrepancyid = 3).count()
    Wrong = TdSupervisorData.objects.filter(transaction_number__typeofdiscrepancyid = 4).count()
    Mix = TdSupervisorData.objects.filter(transaction_number__typeofdiscrepancyid = 5).count()
    Po = TdSupervisorData.objects.filter(transaction_number__typeofdiscrepancyid = 6).count()
    return render(request,'Home/Home.html',{'Today':Today, 'week':week, 'month':month, 'year':year, 'all':all, 'short':short, 'Over':Over, 'Wrong':Wrong, 'Mix':Mix, 'Po':Po})
def login(request):
    return render(request,'Home/login.html')
#Shipment Form
def Shipmentform(request):
    record = TdDiscrepancyrecordform.objects.all().order_by('-transaction_number')
    return render(request,'Shipmentform/Shipmentform.html' , {'records':record})
def Addform(request):
    #Master Table
    area = TdArea.objects.all()
    Mode = JdModeoftransportation.objects.all()
    Invoice = JdDamageuom.objects.all()
    Type = TdTypeofdiscrepancy.objects.all()
    #Date
    currentdate = date.today()
    formatDate = currentdate.strftime("%A/%B/%Y")
    WDweek = currentdate.strftime("%Y-%m-%d")
    #Save Data
    form = shipmentrecord
    if 'submit' in request.POST: 
        form = shipmentrecord(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.status= 'Submitted'
            f.submitby = 'User'
            f.save()
            messages.success(request, 'Your form was Submit successfully')
            return redirect('Shipmentform')
        else:
            messages.warning(request, 'Please correct Your form')
            return HttpResponse('UR form get some Error')
    if 'save' in request.POST: 
        form = shipmentrecord(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.status= 'Saved'
            f.submitby = 'User'
            f.save()
            messages.success(request, 'Your form was Save successfully')
            return redirect('Shipmentform')
        else:
            messages.warning(request, 'Please correct your form')
            return HttpResponse('UR form get some Error')
    return render(request,'Shipmentform/Addform.html',{'areas':area, 'Modes':Mode, 'Invoices':Invoice, 'Types':Type, 'WDweek':WDweek  })
def AddData(request, pk):
    #Master Table
    area = TdArea.objects.all()
    Mode = JdModeoftransportation.objects.all()
    Invoice = JdDamageuom.objects.all()
    Type = TdTypeofdiscrepancy.objects.all()
    AddData = TdDiscrepancyrecordform.objects.get(transaction_number = pk)
    #Mastertable
    form = update(instance=AddData)
    if request.method=='POST':
        form = update(request.POST, request.FILES, instance=AddData)
        if form.is_valid():
            f= form.save(commit=False)
            f.status= 'Submitted'
            f.save()
            messages.success(request, 'You have add Data Successfully')
            return redirect('Shipmentform')
        else:
            messages.warning(request, 'You have got some errors')
            return HttpResponse('Your Data get some Errors')
    return render(request,'Shipmentform/AddData.html', {'form':form,'AddData':AddData,'areas':area, 'Modes':Mode, 'Invoices':Invoice, 'Types':Type  })
#Supervisor
def Action_cause(request):
    record = TdSupervisorData.objects.all()
    return render(request, 'Supervisor/Action&cause.html', {'records':record})
def Action_Shipmentform(request):
    record = TdDiscrepancyrecordform.objects.filter(status="Submitted", status1__isnull=True)
    return render(request, 'Supervisor/Action_Shipmentform.html', {'records':record})
def AddAction(request, pk):
    currentdate = datetime.today()
    WDweek = currentdate.strftime("%Y-%m-%d")
    Action = TdAction.objects.all()
    AddAction = TdDiscrepancyrecordform.objects.get(transaction_number = pk)
    form = Action_(instance=AddAction)
    form1 = Actionform
    if request.method=='POST':
        form1 = Actionform(request.POST, request.FILES)
        form = Action_(request.POST, request.FILES, instance=AddAction)
        if form.is_valid() and form1.is_valid:
            f= form.save(commit=False)
            f.status1= 'Add'
            f.save()
            H= form1.save(commit=False)
            H.report_by='User'
            H.save()
            return redirect('Action')
        else:
            return HttpResponse('Your Data get some Errors')
    return render(request, 'Supervisor/AddAction.html',{'form':form,'AddAction':AddAction,'WDweek':WDweek, 'Actions':Action, })
#Dashboard
def Dash(request): 
    record = TdSupervisorData.objects.all()
    my_date = date.today()
    this_month = datetime.now().month
    year, week_num, day_of_week = my_date.isocalendar()
    Today = TdSupervisorData.objects.filter(report_date=str(my_date)).count()
    week = TdSupervisorData.objects.filter(report_date__week=str(week_num)).count()
    month = TdSupervisorData.objects.filter(report_date__month=str(this_month)).count()
    year = TdSupervisorData.objects.filter(report_date__year=str(year)).count()
    all = TdSupervisorData.objects.all().count()
    return render(request,'Dashboard/Dashboard.html', {'records':record, 'Today':Today, 'week':week, 'month':month, 'year':year, 'all':all})


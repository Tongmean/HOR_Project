from dataclasses import field
from email.utils import format_datetime
from tkinter import Widget
from django import forms
from django.forms import DateInput, ModelForm
from . models import TdDiscrepancyrecordform, TdSupervisorData
#Shipment form
class shipmentrecord(ModelForm):
    class Meta:
        model = TdDiscrepancyrecordform
        fields = '__all__'
        exclude = ['status2']
class update(ModelForm):
    class Meta:
        model = TdDiscrepancyrecordform
        fields = '__all__'
        exclude = ['status2','submitby','submitdate']
        Widgets = {
            'dateofincident': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
class Actionform(ModelForm):
    class Meta:
        model = TdSupervisorData
        fields = '__all__'
class Action_(ModelForm):
    class Meta:
        model = TdDiscrepancyrecordform
        fields = 'status1',
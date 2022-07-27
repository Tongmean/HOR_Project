from django.forms import ModelForm
from .models import TdDiscrepancyrecordform

class shipmentdata(ModelForm):
    class Meta:
        model = TdDiscrepancyrecordform
        fields = '__all__'
        exclude = ['status']

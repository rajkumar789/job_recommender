from django.forms import ModelForm
from django import forms 
from .models import *

class DateWidget(forms.DateInput):
    input_type = 'date'

class JobModelForm(ModelForm):
    deadline = forms.DateField(widget=DateWidget())
    class Meta:
        model = Job
        fields = '__all__'
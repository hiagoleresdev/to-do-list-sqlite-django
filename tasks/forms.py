from django import forms
from django import forms
from django.forms.models import ModelForm 

from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'



from django import forms
from .models import BusinessPlan

class BusinessPlanForm(forms.ModelForm):
    class Meta:
        model = BusinessPlan
        fields = '__all__'

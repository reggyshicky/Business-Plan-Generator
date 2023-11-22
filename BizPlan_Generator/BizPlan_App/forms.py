from django import forms
from .models import BusinessPlan

class BusinessPlanForm(forms.ModelForm):
    class Meta:
        model = BusinessPlan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['industry'].widget.attrs['placeholder'] = (
            'Enter the industry'
        )
        self.fields['target_market'].widget.attrs['placeholder'] = (
            'Describe your target market in detail. Who are your customers?'
        )
        self.fields['unique_selling_proposition'].widget.attrs['placeholder'] = (
            'What sets your business apart?'
        )
        self.fields['specific_requirements'].widget.attrs['placeholder'] = (
            'List specific requirements or unique features your business needs'
        )
        self.fields['goals_and_objectives'].widget.attrs['placeholder'] = (
            'What are your business goals and objectives? Be specific.'
        )
        self.fields['additional_information'].widget.attrs['placeholder'] = (
            'Any additional information you would like to provide'
        )

from django import forms
from .models import Feedback

class CreateFeedbackForm(forms.ModelForm):
    class Meta:
        model  = Feedback
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Your Full Name',
        })
        
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'maxlength': '50',
            'placeholder': 'Your Email Address',
        })
        
        self.fields['remarks'].widget.attrs.update({
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'Any remarks? Type here ...',
        })
from django import forms
from .models import ContactResponse

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactResponse
        fields = '__all__'
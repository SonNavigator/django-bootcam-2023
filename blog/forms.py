from django import forms 
from .models import Contact 


class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact 
        fields = ["subject", "sender", "email", "detail"]
        
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control col-xl-4'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-4'
            }),
            'sender': forms.TextInput(attrs={
                'class': 'form-control col-xl-4'
            }),
            'detail': forms.Textarea(attrs={
                'class': 'form-control col-xl-4'
            })
        }
from .models import *
from django import forms


class MessageForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'info', 'contact']
        model = Messages
from django import forms
from .models import Message


class MessageForm(forms.ModelForm):

    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name',
    }))
    email = forms.CharField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email',
    }))
    who_is_you = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Who is you',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'col': '30',
        'row': '7',
    }))

    class Meta:
        model = Message
        fields = ['name', 'email', 'who_is_you', 'message']


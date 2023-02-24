from django.core import validators
from django import forms
from .models import User

class TaskList(forms.ModelForm):
    class Meta:
        model = User
        fields = ['title','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
           # 'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        }
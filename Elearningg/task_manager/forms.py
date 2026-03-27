from django import forms
from .models import Task_details

class Task_form(forms.ModelForm):
    class Meta:
        model = Task_details
        fields = [
            'task_title',
            'description',
            'subject',
            'due_date',
            'priority',
            'isCompelete'
        ]
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'isCompelete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
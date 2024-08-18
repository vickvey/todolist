# frontend/forms.py
from django import forms
from core_api.models import Task  # Adjust this import based on your app structure

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']  # Adjust fields based on your model
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title must be at least 3 characters long.')
        return title

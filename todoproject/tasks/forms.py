from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority", "category"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Enter task description"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }

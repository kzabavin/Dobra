from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
        'compleat', 
        'title', 
        'note', 
        'folder', 
        'start_time', 
        'deadline',
        'priority',
        'project'
        ]
        widgets = {
            'start_time': forms.SelectDateWidget(),
            'deadline': forms.SelectDateWidget()
        }
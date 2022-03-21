from django import forms

from .models import Task

from tempus_dominus.widgets import DateTimePicker


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
            'start_time': DateTimePicker(),
            'deadline': DateTimePicker()
        }

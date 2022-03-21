from django import forms

from .models import Project

from tempus_dominus.widgets import DateTimePicker


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'compleat',
            'title',
            'note',
            'start_time',
            'context',
            'goal',
            'deadline'
        ]
        widgets = {
            'start_time': DateTimePicker(),
            'deadline': DateTimePicker()
        }

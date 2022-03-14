from django import forms

from .models import Project

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
            'start_time': forms.SelectDateWidget(),
            'deadline': forms.SelectDateWidget()
        }
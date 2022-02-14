from django import forms

from .models import Task

class TaskForm(forms.Form):

    compleat = forms.CheckboxInput()
    title = forms.CharField()
    note = forms.Textarea()

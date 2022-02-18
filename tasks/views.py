from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView

# Create your views here.
from django.http import HttpResponse

from tasks.models import Task


def tasklist(request):
    return render(request, 'tasklist.html', {'tasks': Task.objects.all() })
    
def taskform(request):
    return render(request, 'taskform.html') # new?


# https://python-scripts.com/django-forms
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = ['compleat', 
    'title', 
    'note', 
    'folder', 
    'start_time', 
    'deadline',
    'priority',
    'project']


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
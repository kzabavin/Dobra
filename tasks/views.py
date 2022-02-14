from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
from django.http import HttpResponse

from tasks.models import Task


def tasklist(request):
    return render(request, 'tasklist.html', {'tasks': Task.objects.all() })
    
def taskform(request):
    return render(request, 'taskform.html') # new?
    

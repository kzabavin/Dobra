from dataclasses import fields
from pyexpat import model
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Context as CRUDModel


def modellist(request):
    return render(request, 'list.html', {'objects': CRUDModel.objects.all() })
    

class ModelCreateView(CreateView):
    model = CRUDModel
    template_name = 'create.html'
    fields = [
        'compleat', 
        'title', 
        'note', 
        'folder'
    ]


class ModelDetailView(DetailView):
    model = CRUDModel
    template_name = 'read.html'


class ModelUpdateView(UpdateView):
    model = CRUDModel
    template_name = 'update.html'
    fields = [
        'compleat', 
        'title', 
        'note', 
        'folder'
    ]


class ModelDeleteView(DeleteView):
    model = CRUDModel
    template_name = 'delete.html'
    success_url = reverse_lazy(modellist)

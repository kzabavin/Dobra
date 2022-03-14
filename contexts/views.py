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
    return render(request, 'contexts/list.html', {'objects': CRUDModel.objects.all() , 'name': CRUDModel.__name__})
    

class ModelCreateView(CreateView):
    model = CRUDModel
    template_name = 'create.html'
    fields = ['title']


class ModelDetailView(DetailView):
    model = CRUDModel
    template_name = 'contexts/read.html'


class ModelUpdateView(UpdateView):
    model = CRUDModel
    template_name = 'contexts/update.html'
    fields = ['title']


class ModelDeleteView(DeleteView):
    model = CRUDModel
    template_name = 'delete.html'
    success_url = reverse_lazy(modellist)

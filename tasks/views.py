from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the Dobra.</h1>")
    

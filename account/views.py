#from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _

#from .forms import LoginForm

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})
    #return 

    
# # Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse(_('Authenticated successfully'))
#                 else:
#                     return HttpResponse(_('Disabled account'))
#             else:
#                 return HttpResponse(_('Invalid login'))
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
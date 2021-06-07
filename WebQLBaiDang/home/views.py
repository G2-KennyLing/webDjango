
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request):
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, 'pages/register.html', {'form': form})


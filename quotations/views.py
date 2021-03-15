from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import AddNewClientForm
from .models import Client
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.template.loader import render_to_string


# AUTH RELATED FUNCTIONS
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'quotations/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'quotations/loginuser.html', {'form':AuthenticationForm(), 'error': 'Username and Password did not match!'})
        else:
            login(request, user)
            return redirect('createquotation')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')

# QUOTATION RELATED FUNCTIONS

# HOMEPAGE view
@login_required
def home(request):
    return redirect('createquotationstep1')

# create quotation main view
@login_required
def createquotationstep1(request):
    if request.method == "POST" and 'newclient' in request.POST:
        try:
            form = AddNewClientForm(request.POST)
            form.save()
            # print(form)
            return render(request, 'quotations/create_step2.html', {'form': form})
        except ValueError:  # if text exceeds max length
            return render(request, 'quotations/create_step1.html', {'form': AddNewClientForm(), 'error': 'Bad data passed in!'})
    else:
        return render(request, 'quotations/create_step1.html')
        


@login_required
def createquotationstep2(request):
    if request.method == "GET":
        return render(request, 'quotations/create_step2.html')
@login_required
def createquotationstep3(request):
    if request.method == "GET":
        return render(request, 'quotations/create_step3.html')




# search quotation main view
@login_required
def searchquotation(request):
    return render(request, 'quotations/search.html')

# all clients list view
@login_required
def clientslist(request):
    return render(request, 'quotations/clients.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# from .forms import TodocreateForm
# from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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
@login_required
def home(request):
    return redirect('createquotation')

@login_required
def createquotation(request):
    return render(request, 'quotations/create.html')

@login_required
def searchquotation(request):
    return render(request, 'quotations/search.html')


@login_required
def clientslist(request):
    return render(request, 'quotations/clients.html')

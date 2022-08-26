from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import  Uploads,  schedule ,Final ,assignment
from django.http import FileResponse, request

import io  
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.core.files.storage import FileSystemStorage

def index(response):
    return render(response ,'core/index.html')

def profile(response):
    return render(response ,'core/inner-page.html')

def index_sch(request):
    all_schedule = schedule.objects.all()
    all_final = Final.objects.all()
    context ={
        'all_schedule' : all_schedule,
        'all_final' : all_final,
    }
    return render(request, 'core/inner-page.html' ,context)

def assignment_ass(request):
    all_assi = assignment.objects.all()
    context ={
        'all_assi' : all_assi 
    }  
    return render(request ,'core/assignment.html' ,context) 
    
def material_stu(request):
    obj = Uploads.objects.all()
    context ={
        'obj':obj
    }   
    return render(request ,'core/uploads.html' ,context)             
    
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=username, password=password)
           login(request,user)
           return redirect('/profile')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'core/login.html', context)

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'core/index.html')

def profile_signed(request):
    signed = profile.objects.filter(User)
    context ={
        signed : 'signed'
    }
    return render(request , 'core/inner-page.html' , context)


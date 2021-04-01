from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import models
from django.contrib.auth import login, logout
#from django.http import httpResponse


# Create your views here.
def login(request):
    if request.method =="POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'logout.html')
        else: 
            return render(request, 'user.html',  {'error': "Invalid Login Credentials."})
    else:
        return render(request, 'user.html')

def signup(request):
    if request.method == "POST":
        #to create a user
        if request.POST['psw'] == request.POST['psw-repeat']:
            #check wheater user valid or not
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'singup.html', {'error': "Email has alraedy been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['psw'])
                user.save()
                auth.login(request, user)
                return redirect('/login')
        else:
            return render(request,'singup.html', {'error': "Password doen't Matched"})
    else:
        return render(request, 'singup.html') 
def logout(request):
    auth.logout(request)
    return redirect('/login')

def home(request):
    return render(request,'1.html')
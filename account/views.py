from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import *
# Create your views here.
def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    context = {'page':page}
    return render(request, 'account/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = RegisterForm()
    if request.method == 'POST':
       form=RegisterForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('dashboard')
    context = {'form':form, 'page':page}
    return render(request, 'account/login_register.html', context)
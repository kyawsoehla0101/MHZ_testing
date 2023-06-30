from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def homePage(request):
    new_search = request.GET.get('search') if request.GET.get('search') != None else ''
    coffees = Coffee.objects.filter(
        Q(name__contains = new_search)
    )
    context = {'coffees':coffees}
    return render(request, 'blog/home.html', context)


@login_required(login_url='login')
def indexPage(request):
    page = "create"
    forms = CoffeeForm()
    coffees = Coffee.objects.all()
    if request.method == "POST":
        form = CoffeeForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    context = {'page':page,'forms':forms, 'coffees':coffees}
    return render(request, 'blog/index.html', context)

@login_required(login_url='login')
def editPage(request,pk):
    page = "edit"
    coffees = Coffee.objects.all()
    coffee = Coffee.objects.get(id=pk)
    forms = CoffeeForm(instance=coffee)
    if request.method == "POST":
        form = CoffeeForm(request.POST, request.FILES, instance=coffee)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    context = {'page':page, 'forms':forms, 'coffees':coffees}
    return render(request, 'blog/index.html', context)

@login_required(login_url='login')
def deletePage(request, pk):
    coffee = Coffee.objects.get(id=pk)
    if request.method == "POST":
        coffee.delete()
        return redirect('dashboard')
    context = {'coffee':coffee}
    return render(request, 'blog/delete.html', context)


from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ClientForm

def index(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/about.html')

def basket(request):
    return render(request,'main/basket.html')




def catalog(request):
    return render(request,'main/catalog.html')


def user(request):
    error=''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Дані введені не правильно'

    form= ClientForm()
    context= {
        'form': form,
        'error': error
    }
    return render(request, 'main/user.html', context)


from django.shortcuts import render
from .models import *

def home(request):
    home = Home.objects.first()
    contex = {
        'home': home,
    }
    return render(request, 'index.html', contex)


def about(request):
    about =  Haqqimizda.objects.first()
    team = Team.objects.all()

    contex = {
        'about': about,
        'team': team,
    }


    return render(request, 'haqqımızda.html', contex)


def products(request):
    products = Mehsullar.objects.all()

    contex = {
        'products' : products,
    }

    return render(request, 'məhsullar.html', contex)
# Create your views here.

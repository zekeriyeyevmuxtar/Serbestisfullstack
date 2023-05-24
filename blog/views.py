from django.shortcuts import render
from .models import *
from django.db.models import Q,Count #filtreleme opsiyonları için import ettik


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
    categories = Category.objects.all()
    products = Mehsullar.objects.all()

    selected_category_id = request.GET.get('category_id')
    if selected_category_id:
        products = products.filter(category_id=selected_category_id)

    context = {
        'categories': categories,
        'products': products,
        'selected_category_id': selected_category_id,
    }
    return render(request, 'məhsullar.html', context)
# Create your views here.

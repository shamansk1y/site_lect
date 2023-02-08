from django.shortcuts import render
from .models import Category, Dish
from django.http import HttpResponse

def main(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    return render(request, 'menu.html', context={
        'categories': categories
    })
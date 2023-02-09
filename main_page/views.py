from django.shortcuts import render
from .models import Category, Dish, Galery, Team
from django.http import HttpResponse

def main(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    gallery = Galery.objects.all()[:8]
    chefs = Team.objects.filter(is_visible=True)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'gallery': gallery,
        'chefs': chefs,
    })
from django.contrib import admin
from .models import Category, Dish, Team, Galery, Booking, About

class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']

    inlines = [DishAdmin]

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'desc', 'price', 'photo', 'category', 'is_special']
    list_filter = ['category', 'is_special', 'is_visible']
    list_editable = ['position', 'is_visible', 'price', 'is_special']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_editable = ['position', 'is_visible']
    list_display = ['name_staff', 'position', 'is_visible']
    list_display_links = None

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    model = Galery
    list_editable = ['position', 'is_visible']
    list_display = ['title', 'position', 'is_visible']
    list_display_links = None
    list_filter = ['position']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = ['book_num', 'date', 'time', 'num_of_pers']
    list_editable = ['book_num', 'date', 'time', 'num_of_pers']
    list_display_links = None
    list_filter = ['date']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
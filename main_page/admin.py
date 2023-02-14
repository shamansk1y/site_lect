from django.contrib import admin
from .models import Category, Dish, Team, Galery, Booking, About, WhyUs, \
    Reservation, Slider, ContactUs, ContactInfo, Footer


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
    list_editable = ['name_staff', 'position', 'is_visible', 'profession', 'staff_photo']
    list_display = ['name_staff', 'position', 'is_visible', 'profession', 'staff_photo']
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

@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    model = WhyUs
    list_display = ['name', 'position', 'desc', 'is_visible']
    list_editable = ['name', 'position', 'desc', 'is_visible']
    list_display_links = None

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['name', 'phone', 'persons', 'message', 'date', 'is_processed']
    list_editable = ['is_processed']
    list_display_links = None
    list_filter = ['date']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['title', 'position', 'photo', 'is_visible', 'h_1', 'desc']
    list_editable = ['title', 'position', 'photo', 'is_visible', 'h_1', 'desc']
    list_display_links = None
    list_filter = ['position']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['name', 'email', 'subject_mes', 'message', 'date', 'is_processed']
    list_editable = ['is_processed']
    list_display_links = None
    list_filter = ['date']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    model = ContactInfo
    list_display = ['location', 'location_text', 'open_hours', 'open_hours_text', 'email', 'email_text', 'phone', 'phone_text']
    list_editable = ['location', 'location_text', 'open_hours', 'open_hours_text', 'email', 'email_text', 'phone', 'phone_text']
    list_display_links = None


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    model = Footer
    list_display = ['name', 'desc', 'twitter', 'facebook', 'instagram', 'google_plus', 'linkedin']
    list_editable = ['name', 'desc', 'twitter', 'facebook', 'instagram', 'google_plus', 'linkedin']
    list_display_links = None



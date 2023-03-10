from django.shortcuts import render, redirect
from .models import Category, Dish, Galery, Team, WhyUs, Slider, ContactInfo, Footer, Testimonials, \
    About, Events, Reservation
from .forms import ReservationForm, ContactUsForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()



def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        form_contact_us = ContactUsForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')
        if form_contact_us.is_valid():
            form_contact_us.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    gallery = Galery.objects.all()[:8]
    chefs = Team.objects.filter(is_visible=True)
    why_us = WhyUs.objects.all()[:3]
    form_reserve = ReservationForm()
    slider = Slider.objects.filter(is_visible=True)
    form_contact_us = ContactUsForm()
    contact_info = ContactInfo.objects.get()
    footer = Footer.objects.get()
    testimonials = Testimonials.objects.filter(is_visible=True)
    about = About.objects.get()
    events = Events.objects.filter(is_visible=True)
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated


    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'gallery': gallery,
        'chefs': chefs,
        'form_reserve': form_reserve,
        'why_us': why_us,
        'slider': slider,
        'form_contact_us': form_contact_us,
        'contact_info': contact_info,
        'footer': footer,
        'testimonials': testimonials,
        'about': about,
        'events': events,
        'user_manager': user_manager,
        'user_auth': user_auth,
    })

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:list_reservations')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_reservation(request):
    messages = Reservation.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={'reservations': messages})
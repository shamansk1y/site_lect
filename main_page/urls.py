from django.urls import path
from .views import main, update_reservation, list_reservation

app_name = 'main_page'

urlpatterns = [
    path('', main),
    path('manager/update_reserve/<int:pk>', update_reservation, name='update_reservation'),
    path('manager/reserve_list/', list_reservation, name='list_reservations'),
]
from django.urls import path

from .views import Reservation, Reservations, MakeReservation


urlpatterns = [
    path('reservations', Reservations.as_view(), name='get-reservations'),
    path('reservation/<int:id>', Reservation.as_view(), name='get-reservation'),
    path('make-reservation', MakeReservation.as_view(), name='make-reservation')
]
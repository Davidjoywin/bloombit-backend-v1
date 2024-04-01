from django.urls import path

from .views import Reservation, Reservations, UserReservations, MakeReservation


urlpatterns = [
    path('reservations', Reservations.as_view(), name='get-reservations'),
    path('user/reservations', UserReservations.as_view(), name='auth-user-reservation'),
    path('reservation/<int:id>', Reservation.as_view(), name='get-reservation'),
    path('make-reservation', MakeReservation.as_view(), name='make-reservation')
]
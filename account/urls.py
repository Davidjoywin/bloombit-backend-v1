from django.urls import path

from .views import Auth, GetUser, CreateUser, GetProfessional

urlpatterns = [
    path('register', CreateUser.as_view(), name='register'),
    path('auth', Auth.as_view(), name='login'),
    path('<int:id>', GetUser.as_view(), name='get-user'),
    path('<int:id>/professional', GetProfessional.as_view(),  name='update-professional'),
]

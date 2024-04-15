from django.urls import path

from .views import (
    Auth, GetUser, AuthenticatedUser,
    CreateUser, GetProfessional, KPI
)

urlpatterns = [
    path('register', CreateUser.as_view(), name='register'),
    path('auth', Auth.as_view(), name='login'),
    path('<int:id>', GetUser.as_view(), name='get-user'),
    path('user', AuthenticatedUser.as_view(), name='auth-user'),
    path('<int:id>/professional', GetProfessional.as_view(),  name='update-professional'),
    path('kpi', KPI.as_view(), name='KPI')
]

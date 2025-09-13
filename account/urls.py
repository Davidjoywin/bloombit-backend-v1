from django.urls import path

from .views import (
    Auth, GetUser, AuthenticatedUser, CreateUser, KPI, CheckAuthStatus
)

urlpatterns = [
    path('test-auth', CheckAuthStatus.as_view()),
    path('register', CreateUser.as_view(), name='register'),
    path('auth', Auth.as_view(), name='login'),
    path('<int:id>', GetUser.as_view(), name='get-user'),
    path('user', AuthenticatedUser.as_view(), name='auth-user'),
    path('kpi', KPI.as_view(), name='KPI'),

    # specialist account 
    # path('register-specialist', MedicalSpecialist.as_view(), name='register-specialist'),
]

from django.urls import path
from .views import (
    Category, GetCategories, CreateMedicalSpecialist,
    MedicalSpecialistView, AllMedicalSpecialistView
)

urlpatterns = [
    path('category/<str:slug>', Category.as_view()),
    path('category/all', GetCategories.as_view()),
    path('medical-specialist/create', CreateMedicalSpecialist.as_view()),
    path('medical-specialist/<int:id>', MedicalSpecialistView.as_view()),
    path('medical-specialist/all', AllMedicalSpecialistView.as_view())
]

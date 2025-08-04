from django.urls import path
from .views import (
    Category, GetCategories, CreateMedicalSpecialist,
    MedicalSpecialistView, AllMedicalSpecialistView,
    MedicalSpecialistByCategoryView
)

urlpatterns = [
    path('categories', GetCategories.as_view()),
    path('category/<str:slugged_name>', Category.as_view()),
    path('specialist/create', CreateMedicalSpecialist.as_view()),
    path('specialist/category/<str:slugged_name>', MedicalSpecialistByCategoryView.as_view()),
    path('specialist/<int:id>', MedicalSpecialistView.as_view()),
    path('specialist', AllMedicalSpecialistView.as_view())
]

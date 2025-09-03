from django.urls import path
from .views import (
    Category, GetCategories, CreateMedicalSpecialist,
    MedicalSpecialistView, AllMedicalSpecialistView,
    MedicalSpecialistByCategoryView, CreateCategory, GetSpecialist
)

urlpatterns = [
    path('categories', GetCategories.as_view()),
    path('category/<int:id>', Category.as_view()),
    path('category/create', CreateCategory.as_view()),
    path('all-specialists', AllMedicalSpecialistView.as_view()),
    path('specialist/create', CreateMedicalSpecialist.as_view()),
    # path('specialist/<int:id>', GetSpecialist.as_view(),  name='specialist'),
    path('specialist/<str:id>', MedicalSpecialistView.as_view()),
    path('specialist/category/<str:slugged_name>', MedicalSpecialistByCategoryView.as_view()),
]

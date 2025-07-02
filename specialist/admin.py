from django.contrib import admin

from .models import (
    Specialization, 
    MedicalSpecialist, 
    AvailabilityTime, 
    Education,
    Language
)

admin.site.register(Language)
admin.site.register(Education)
admin.site.register(Specialization)
admin.site.register(AvailabilityTime)
admin.site.register(MedicalSpecialist)
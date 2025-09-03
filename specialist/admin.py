from django.contrib import admin

from .models import (
    Specialization, 
    MedicalSpecialist, 
    AvailabilityTime
)

admin.site.register(Specialization)
admin.site.register(AvailabilityTime)
admin.site.register(MedicalSpecialist)
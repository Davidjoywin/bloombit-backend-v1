from django.contrib import admin

from .models import (
    Specialization, 
    MedicalSpecialist, 
    AvailabilityTime, 
    Education
)

admin.site.register(Specialization)
admin.site.register(MedicalSpecialist)
admin.site.register(AvailabilityTime)
admin.site.register(Education)
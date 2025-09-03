from django.contrib import admin

from .models import (
    UserProfile, SecurityMode
)


admin.site.register(UserProfile)
admin.site.register(SecurityMode)

# admin.site.register(MedicalSpecialist)
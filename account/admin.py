from django.contrib import admin

from .models import (
    UserProfile, SecurityMode, RegisterSpecialist
)


admin.site.register(UserProfile)
admin.site.register(SecurityMode)

admin.site.register(RegisterSpecialist)
from django.contrib import admin

from .models import UserProfile, Professional, SecurityMode


admin.site.register(UserProfile)
admin.site.register(SecurityMode)
admin.site.register(Professional)
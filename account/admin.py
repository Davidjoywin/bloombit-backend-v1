from django.contrib import admin

from .models import (
    UserProfile, SecurityMode, SpecialistPersonalInformations, SpecialistProfessionalDetails, 
    SpecialistVerificationDocuments, SpecialistAgreements, RegisterSpecialist
)


admin.site.register(UserProfile)
admin.site.register(SecurityMode)

admin.site.register(SpecialistPersonalInformations)
admin.site.register(SpecialistProfessionalDetails)
admin.site.register(SpecialistVerificationDocuments)
admin.site.register(SpecialistAgreements)
admin.site.register(RegisterSpecialist)
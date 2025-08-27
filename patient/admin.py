from django.contrib import admin
from .models import Patient, Vital, MedicalCondition, Medication, LabResult, Allergy, ClinicalNote

admin.site.register(Vital)
admin.site.register(Patient)
admin.site.register(MedicalCondition)
admin.site.register(Medication)
admin.site.register(LabResult)
admin.site.register(Allergy)
admin.site.register(ClinicalNote)

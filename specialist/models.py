from django.db import models
from uuid import uuid4

from account.models import (
    SpecialistPersonalInformations, SpecialistProfessionalDetails, 
    SpecialistAgreements, SpecialistVerificationDocuments, UserProfile
)

class Specialization(models.Model):
    icon_choices = [
        ("heart", "Heart"),
        ("brain", "Brain"),
        ("baby", "Baby"),
        ("bone", "Bone"),
        ("scan", "Scan"),
        ("brain_circuit", "BrainCircuit"),
        ("eye", "Eye"),
        ("stethoscope", "Stethoscope"),
        ("lungs", "Lungs"),
        ("flask", "Flask"),
        ("microscope", "Microscope"),
        ("laptop", "Laptop"),
    ]
    name = models.CharField(max_length=30, unique=True)
    slugged_name = models.SlugField(max_length=30)
    icon = models.CharField(max_length=15, choices=icon_choices)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    def sluggify(self):
        return '-'.join(self.name.lower().split(' '))
    
class AvailabilityTime(models.Model):
    hour_daily = models.DateTimeField()
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Available Time: {self.hour_daily}:00"
    

# class MedicalSpecialist(models.Model):
#     prefix = models.CharField(default="Dr", max_length=5, blank=True)
#     name = models.CharField(max_length=25)
#     education = models.OneToOneField(Education, on_delete=models.CASCADE)
#     location = models.CharField(max_length=50)
#     years_experience = models.PositiveIntegerField()
#     about = models.TextField()
#     specialization = models.ForeignKey(to=Specialization, on_delete=models.CASCADE)
#     date_joined = models.DateField(auto_now=True, auto_created=True)
#     is_available = models.BooleanField(default=False)
#     # languages = models.ManyToManyField(to=Language)

#     def __str__(self):
#         return self.name

class MedicalSpecialist(
    SpecialistPersonalInformations, SpecialistProfessionalDetails,
    SpecialistVerificationDocuments, SpecialistAgreements
):
    id = models.UUIDField(primary_key=True, default=uuid4, auto_created=True, blank=True)
    prefix = models.CharField(max_length=3, default="Dr.")
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    years_of_experience = models.IntegerField()
    about = models.TextField()
    # personal_information = models.OneToOneField(SpecialistPersonalInformations, on_delete=models.CASCADE)
    # professional_details = models.OneToOneField(SpecialistProfessionalDetails, on_delete=models.CASCADE)
    # verification_documents = models.OneToOneField(SpecialistVerificationDocuments, on_delete=models.CASCADE)
    # agreements = models.OneToOneField(SpecialistAgreements, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Language(models.Model):
    langs = [
        ("english", "English"),
        ("spanish", "Spanish"),
        ("french", "French"),
    ]
    lvl = [
        ('beginner', "Beginner"),
        ("fluent", "Fluent"),
        ("expert", "Expert"),
        ("native", "Native")
    ]
    medical_specialist = models.ForeignKey(to="MedicalSpecialist", on_delete=models.CASCADE)
    language = models.CharField(choices=langs, max_length=20)
    level = models.CharField(choices=lvl, max_length=8)
    
    def __str__(self):
        return self.language
    
class Education(models.Model):
    medical_specialist = models.ForeignKey(MedicalSpecialist, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=20)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return f"Education: {self.school_name}. Major: {self.major}"
    
# class Professional(models.Model):
#     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     field = models.CharField(max_length=25)
#     summary = models.CharField(max_length=50)
#     booked = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.user.get_full_name() or self.user.username} => {self.field}"

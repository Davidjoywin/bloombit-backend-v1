from django.db import models
from uuid import uuid4

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
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    icon = models.CharField(max_length=15, choices=icon_choices)
    slugged_name = models.SlugField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class AvailabilityTime(models.Model):
    hour_daily = models.DateTimeField()
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Available Time: {self.hour_daily}:00"
    
class Education(models.Model):
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=20)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return f"Education: {self.school_name}. Major: {self.major}"
    
# class Language(models.Model):
#     langs = [
#         ("english", "English"),
#         ("spanish", "Spanish"),
#         ("french", "French"),
#     ]
#     language = models.CharField(choices=langs, max_length=20)

#     def __str__(self):
#         return self.language

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
    # medical_specialist = models.ForeignKey(to="MedicalSpecialist", on_delete=models.CASCADE)
    language = models.CharField(choices=langs, max_length=20)
    level = models.CharField(choices=lvl, max_length=8)
    
    def __str__(self):
        return self.language
    

class MedicalSpecialist(models.Model):
    prefix = models.CharField(default="Dr", max_length=5, blank=True)
    name = models.CharField(max_length=25)
    education = models.OneToOneField(Education, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    years_experience = models.PositiveIntegerField()
    about = models.TextField()
    specialization = models.ForeignKey(to=Specialization, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True, auto_created=True)
    is_available = models.BooleanField(default=False)
    languages = models.ManyToManyField(to=Language)

    def __str__(self):
        return self.name
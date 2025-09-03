from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    types = [
        ("patient", "Patient"),
        ("specialist", "Specialist")
    ]
    phone_no = models.CharField(max_length=15, null=True)
    account_type = models.CharField(max_length=14, default='patient', choices=types)
    
    def __str__(self):
        return self.username
    
class SecurityMode(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    login_alert = models.BooleanField(default=True)

    def __str__(self):
        return "Security Mode"
    
class SpecialistPersonalInformations(models.Model):
    class Meta:
        abstract = True

    genger_choices = [
        ("male", "Male"),
        ("female", "Female"),
        ("not specified", "Not Specified"),
    ]
    firstname = models.CharField(max_length=25, blank=False, null=False)
    lastname = models.CharField(max_length=25, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    DOB = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=15, choices=genger_choices, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=20, blank=False, null=False)
    state_or_province = models.CharField(max_length=20, blank=False, null=False)
    postal_code = models.CharField(max_length=15, blank=False, null=False)
    country = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return "Specialist Personal Informations"

# class ServiceOffered(models.Model):
#     in_person_consultation = models.BooleanField(default=False)
#     surgery = models.BooleanField(default=False)
#     emergency_care = models.BooleanField(default=False)
#     telemedicine = models.BooleanField(default=False)
#     follow_up_care = models.BooleanField(default=False)
#     preventive_care = models.BooleanField(default=False)

# class AppointmentAvailability(models.Model):
#     time_available = [
#         ('morning', "Morning (7am-12pm)"),
#         ("afternoon", "Afternoon (12pm-5pm)"),
#         ("evening", "Evening (5pm-10pm)"),
#         ("full day", "Full Day (7am-10pm)"),
#         ("not available", "Not Available")
#     ]
#     weekday = models.CharField(choices=time_available, max_length=15)
#     weekend = models.CharField(choices=time_available, max_length=15)

time_availability = {
    "morning": [i for i in range(7, 13)], # time: 7,8,9,10,11,12
    "afternoon": [i for i in range(12, 18)], # time: 13,14,15,16,17 
    "evening": [i for i in range(17, 23)], # time: 18,19,20,21,22,
    "full-day": [i for i in range(7, 23)], # time: 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22
    "not-available": []
}

class SpecialistProfessionalDetails(models.Model):
    class Meta:
        abstract = True

    duration_choices = [
        (15, "15 mins"), (30, "30 mins"), (45, "45 mins"), (60, "60 mins"), 
        (90, "90 mins"), (120, "120 mins")
    ]
    time_available = [
        ('morning', "Morning (7am-12pm)"),
        ("afternoon", "Afternoon (12pm-5pm)"),
        ("evening", "Evening (5pm-10pm)"),
        ("full-day", "Full Day (7am-10pm)"),
        ("not-available", "Not Available")
    ]
    primary_specialization = models.CharField(max_length=30, blank=False, null=False)
    secondary_specialization = models.CharField(max_length=30, blank=False, null=False)
    highest_medical_qualification = models.CharField(max_length=30, blank=False, null=False)
    medical_license_number = models.CharField(max_length=30, blank=False, null=False)
    years_of_experience = models.CharField(max_length=30, blank=False, null=False)
    current_practice_or_hospital = models.CharField(max_length=30, blank=False, null=False)
    professional_bio = models.CharField(max_length=30, blank=False, null=False)
    # service_offered = models.OneToOneField(ServiceOffered, on_delete=models.CASCADE)
    in_person_consultation = models.BooleanField(default=False)
    surgery = models.BooleanField(default=False)
    emergency_care = models.BooleanField(default=False)
    telemedicine = models.BooleanField(default=False)
    follow_up_care = models.BooleanField(default=False)
    preventive_care = models.BooleanField(default=False)
    # appointment_availability = models.OneToOneField(AppointmentAvailability, on_delete=models.CASCADE);
    weekday_availability = models.CharField(choices=time_available, max_length=15)
    weekend_availability = models.CharField(choices=time_available, max_length=15)
    average_appointment_duration = models.IntegerField(choices=duration_choices)

    def __str__(self):
        return "Specialist Professional Details"
    

class SpecialistVerificationDocuments(models.Model):
    class Meta:
        abstract = True

    profile_photo = models.ImageField(upload_to="./specialist/img", blank=False, null=False)
    government_issued_id = models.ImageField(upload_to="./specialist/img", blank=False, null=False)
    medical_license = models.ImageField(upload_to="./specialist/img", blank=False, null=False)
    medical_degree_certificate = models.ImageField(upload_to="./specialist/img", blank=False, null=False)
    additional_certificate = models.ImageField(upload_to="./specialist/img", blank=False, null=False)

    def __str__(self):
        return "Specialist Verification Documents"

    
class SpecialistAgreements(models.Model):
    class Meta:
        abstract = True

    terms_and_conditions_agreed = models.BooleanField(default=False, blank=False, null=False)
    consent_to_process_data_agreed = models.BooleanField(default=False, blank=False, null=False)
    information_confirmed = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return "Specialist Agreements"
    

from django.db import models
from account.models import UserProfile, RegisterSpecialist, SpecialistPersonalInformations
    
    
class Vital(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    readings = models.JSONField(default=list, blank=True, null=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Patient(SpecialistPersonalInformations):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class MedicalCondition(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    diagnosis_date = models.DateField()
    status = models.CharField(max_length=20)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=50)
    dosage = models.CharField(max_length=30)
    frequency = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    prescribing_doctor = models.ForeignKey(RegisterSpecialist, on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class LabResult(models.Model):
    test_name = models.CharField(max_length=50)
    result = models.TextField()
    date_conducted = models.DateField()
    ordering_doctor = models.ForeignKey(RegisterSpecialist, on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.test_name
    

class ClinicalNote(models.Model):
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(RegisterSpecialist, on_delete=models.CASCADE)
    patient = models.OneToOneField('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Clinical Note for {self.patient.user.username} at {self.created_at}"


class Allergy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    reactions = models.TextField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
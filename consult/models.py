import pytz
from datetime import timedelta, datetime

from django.db import models

from account.models import UserProfile
from patient.models import Patient
from specialist.models import MedicalSpecialist


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialist_assigned = models.ForeignKey(MedicalSpecialist, on_delete=models.CASCADE, related_name="specialist_assigned", blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)  # in minutes
    start_time = models.DateTimeField(auto_created=True)
    end_time = models.DateTimeField(blank=True, null=True)
    recommended_treatment = models.TextField(blank=True, null=True)
    health_condition_summary = models.CharField(max_length=50, blank=True, null=True)
    specialist_of_choice = models.ForeignKey(MedicalSpecialist, on_delete=models.CASCADE, related_name='patient_specialist_choice', blank=True, null=True)
    consult_completed = models.BooleanField(default=False)
    call_link = models.CharField(max_length=25, blank=True, null=True)
    prescription = models.CharField(max_length=35, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patient.username
    
    def _setConsultationDuration(self):
        time = self.start_time + timedelta(minutes=self.duration)
        time = datetime(
            time.year,
            time.month,
            time.day,
            time.hour,
            time.minute,
            time.second,
            time.microsecond,
            tzinfo=pytz.UTC
        )
        # print(time)
        return time
    
    @classmethod
    def makeAppointment(cls, **data):
        consultation = cls.objects.create(**data)
        consultation.end_time = consultation._setConsultationDuration()
        consultation.save()
        return consultation
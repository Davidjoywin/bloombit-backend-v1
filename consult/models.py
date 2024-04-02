import pytz
from datetime import timedelta, datetime

from django.db import models

from account.models import UserProfile, Professional


class Consultation(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    professional_assigned = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="professional_assigned", blank=True, null=True)
    duration = models.IntegerField()
    start_time = models.DateTimeField(auto_created=True, auto_now=True)
    end_time = models.DateTimeField(blank=True, null=True)
    recommended_treatment = models.TextField()
    health_condition_summary = models.CharField(max_length=50)
    professional_of_choice = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='patient_professional_choice', blank=True, null=True)
    consult_done = models.BooleanField(default=False)
    call_link = models.CharField(max_length=25)
    prescription = models.CharField(max_length=35)
    
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
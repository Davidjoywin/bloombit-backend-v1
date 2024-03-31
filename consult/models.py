from datetime import timedelta

from django.db import models

from account.models import UserProfile, Professional


class Consultation(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    professional_assigned = models.ForeignKey(Professional, on_delete=models.CASCADE)
    duration = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    recommended_treatment = models.TextField()
    health_condition_summary = models.CharField(max_length=50)
    professional_of_choice = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='profession_choice', blank=True)
    consult_done = models.BooleanField(default=False)
    call_link = models.CharField(max_length=25)
    prescription = models.CharField(max_length=35)
    
    def __str__(self):
        return self.patient
    
    def _setConsultationDuration(self):
        time = self.start_time + timedelta(self.duration)
        return time
    
    @classmethod
    def makeAppointment(cls, **data):
        consultation = cls.objects.create(**data)
        consultation.end_time = cls()._setConsultationDuration()
        consultation.save()
        return consultation
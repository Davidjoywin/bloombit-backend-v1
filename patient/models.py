from django.db import models
from account.models import UserProfile

class Vital(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    readings = models.JSONField(default=list, blank=True, null=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # vitals = models.ManyToManyField(Vital)

    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    types = [
        ("patient", "patient"),
        ("professional", "professional")
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
    
class Professional(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    field = models.CharField(max_length=25)
    summary = models.CharField(max_length=50)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} => {self.field}"

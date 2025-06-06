from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    images = models.ImageField(verbose_name="specialization image", 
                               upload_to="Images/specialization_img")
    
    def __str__(self):
        return self.name
    
class AvailabilityTime(models.Model):
    hour_daily = models.DateTimeField()
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Available Time: {self.hour_daily}:00"
    
class Education(models.Model):
    school_name = models.CharField(max_length=25)
    major = models.CharField(max_length=15)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return f"Education: {self.school_name}. Major: {self.major}"
    
class Language(models.Model):
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language

class MedicalSpecialist(models.Model):
    class LangLevel(models.Model):
        lvl = [
            ('beginner', "Beginner"),
            ("fluent", "Fluent"),
            ("expert", "Expert"),
            ("native", "Native")
        ]
        medical_specialist = models.ForeignKey(to="MedicalSpecialist", on_delete=models.CASCADE)
        language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
        level = models.CharField(choices=lvl, max_length=8)

    name = models.CharField(max_length=25)
    education = models.OneToOneField(Education, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    years_experience = models.IntegerField(min=0)
    about = models.TextField()
    specialization = models.ForeignKey(to=Specialization, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now=True, auto_created=True)
    hour_daily = models.DateTimeField()
    is_available = models.BooleanField(default=False)
    languages = models.ManyToManyField(to=Language, through=LangLevel)

    def __str__(self):
        return self.name
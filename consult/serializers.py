import random
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer

from patient.models import Patient
from account.models import UserProfile, time_availability
from .models import Consultation, MedicalSpecialist

class ConsultationSerializer(ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"
        extra_kwargs = {
            "patient": {"required": False, "read_only": False},
            "specialist_assigned": {"required": False, "read_only": True},
            "end_time": {"required": False, "read_only": True}
        }
    
    def create(self, validated_data):
        consultation = Consultation.makeAppointment(**validated_data)
        consultation.save()
        return consultation
    
    def validate(self, data):
        request = self.context['request']

        print(request)
        if request.method == "PUT":
            patient = data['patient']
            if request.user.id == patient.id:
                specialists = MedicalSpecialist.objects.filter(booked=False)
                
                if len(specialists) == 0:
                    raise ValidationError({"profession": "No specialist for now"})
                
                # randomly assigned unassigned specialist to patients
                specialist = random.choice(specialists)
                specialist.booked = True
                specialist.save()
                data['specialist_assigned'] = specialist
                specialist_assigned = data.get('specialist_assigned', False)
                patient_specialist_choice = data.get('specialist_of_choice', False)

                if (patient_specialist_choice and (patient_specialist_choice.booked)):
                    raise ValidationError({"specialist": "specialist booked for now"})

                if ((specialist_assigned and (specialist_assigned.user.account_type != "specialist")) or
                    (patient_specialist_choice and (patient_specialist_choice.user.account_type != "specialist"))):
                    raise ValidationError({"specialist": "Account type must be specialist"})
                return data
            raise ValidationError({"User auth": "User not Authenticated"})
        return data
        
    def update(self, instance, validated_data):
        super().update(instance, validated_data)

class MakeReservationSerializer(ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"
        extra_kwargs = {
            "duration": {"required": True},
            "patient": {"required": False, "read_only": True},
            "end_time": {"required": False, "read_only": True},
            "call_link": {"required": False, "read_only": True},
            "consult_completed": {"required": False, "read_only": True},
            "specialist_assigned": {"required": False, "read_only": True},
            "specialist_of_choice": {"required": False, "read_only": False},
        }

    def validate(self, attrs):
        auth_user = self.context['request'].user
        user_profile = UserProfile.objects.get(username=auth_user.username)
        if user_profile.account_type != 'patient':
            raise ValidationError({'user': "Only patient can book appointment"})
        if Patient.objects.filter(user=user_profile).exists():
            attrs['patient'] = Patient.objects.get(user=user_profile)
        else:
            raise ValidationError({'user': 'Patient profile for this user has not been created'})
        start_time = attrs['start_time']
        attrs['end_time'] = start_time + timedelta(minutes=attrs['duration'])

        specialist_of_choice = attrs['specialist_of_choice']
        weekday_available = specialist_of_choice.weekday_availability
        weekend_available = specialist_of_choice.weekend_availability
        end_time = attrs['end_time']
        if end_time.hour not in time_availability[weekday_available]:
            # print(time_availability[weekday_available])
            raise ValidationError({'user': "Specialist is not available at this time"})
        return attrs
    
    def create(self, validated_data):
        consultation = Consultation.makeAppointment(**validated_data)

        return consultation
    
    # def validate(self, data):
    #     request = self.context['request']
    #     if request.user.id == data['patient'].id:
    #         specialist_of_choice = data.get('specialist_of_choice', False)
    #         if specialist_of_choice:
    #             if specialist_of_choice.booked:
    #                 raise ValidationError({"specialist": "specialist booked for now"})
    #             if specialist_of_choice.user.account_type != "specialist":
    #                 raise ValidationError({"specialist": "Account type must be specialist"})
    #         return data
    #     raise ValidationError({"User auth": "User not Authenticated"})  
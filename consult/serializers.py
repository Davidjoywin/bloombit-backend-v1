import random

from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Consultation, Professional

class ConsultationSerializer(ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"
        extra_kwargs = {
            "patient": {"required": False, "read_only": False},
            "professional_assigned": {"required": False, "read_only": True}
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
                professionals = Professional.objects.filter(booked=False)
                
                if len(professionals) == 0:
                    raise ValidationError({"profession": "No professional for now"})
                
                # randomly assigned unassigned professional to patients
                professional = random.choice(professionals)
                professional.booked = True
                professional.save()
                data['professional_assigned'] = professional
                professional_assigned = data.get('professional_assigned', False)
                patient_professional_choice = data.get('professional_of_choice', False)

                if (patient_professional_choice and (patient_professional_choice.booked)):
                    raise ValidationError({"professional": "Professional booked for now"})

                if ((professional_assigned and (professional_assigned.user.account_type != "professional")) or
                    (patient_professional_choice and (patient_professional_choice.user.account_type != "professional"))):
                    raise ValidationError({"professional": "Account type must be professional"})
                return data
            raise ValidationError({"User auth": "User not Authenticated"})
        return data
        
    def update(self, instance, validated_data):
        super().update(instance, validated_data)

class MakeReservationSerializer(ModelSerializer):
    class Meta:
        model = Consultation
        # fields = [
        #     "patient",
        #     "consultation_type",
        #     "preferred_date",
        #     "preferred_time",
        #     "symptoms",
        #     "professional_of_choice"
        # ]
        fields = "__all__"
        extra_kwargs = {
            "patient": {"required": False, "read_only": False},
            "specialist_of_choice": {"required": False, "read_only": False}
        }
    
    def create(self, validated_data):
        consultation = Consultation.makeAppointment(**validated_data)

        consultation.save()
        return consultation
    
    # def validate(self, data):
    #     request = self.context['request']
    #     if request.user.id == data['patient'].id:
    #         professional_of_choice = data.get('professional_of_choice', False)
    #         if professional_of_choice:
    #             if professional_of_choice.booked:
    #                 raise ValidationError({"professional": "Professional booked for now"})
    #             if professional_of_choice.user.account_type != "professional":
    #                 raise ValidationError({"professional": "Account type must be professional"})
    #         return data
    #     raise ValidationError({"User auth": "User not Authenticated"})  
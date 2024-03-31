from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Consultation


class ConsultationSerializer(ModelSerializer):
    class Meta:
        model = Consultation
        fields = "__all__"
    
    def create(self):
        consultation = Consultation.makeAppointment()
        return consultation
    
    def validate(self, validated_data):
        request = self.context['request']
        consultation = get_object_or_404(Consultation, pk=id)
        if request.user.id == consultation.patient.id:
            professional_assigned = validated_data['professional_assigned']
            professional_of_choice = validated_data['professional_of_choice']

            if ((professional_assigned.account_type != "professional") or
                (professional_of_choice.account_type != "professional")):
                raise ValidationError({"professional": "Account type must be professional"})
            return validated_data
        raise ValidationError({"User auth": "User not Authenticated"})
    
    def update(self, instance, validated_data):
        super().update(instance, validated_data)

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ..models import RegisterSpecialist


class RegisterSpecialistSerializer(ModelSerializer):
    # personal_information = SpecialistPersonalInfoSerializer()
    # professional_details = SpecialistProfessionalDetailSerializer()
    # verification_documents = SpecialistVerificationDocumentSerializer()
    # agreements = SpecialistAgreementSerializer()
    
    class Meta:
        model = RegisterSpecialist
        fields = "__all__"
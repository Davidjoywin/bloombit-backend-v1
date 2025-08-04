from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ..models import (
    SpecialistProfessionalDetails, SpecialistPersonalInformations, SpecialistVerificationDocuments, 
    SpecialistAgreements, RegisterSpecialist, AppointmentAvailability, ServiceOffered
)

class SpecialistPersonalInfoSerializer(ModelSerializer):
    class Meta:
        model = SpecialistPersonalInformations
        fields = "__all__"

class SpecialistProfessionalDetailSerializer(ModelSerializer):
    class Meta:
        model = SpecialistProfessionalDetails
        fields = "__all__"

class SpecialistVerificationDocumentSerializer(ModelSerializer):
    class Meta:
        model = SpecialistVerificationDocuments
        fields = "__all__"

class SpecialistAgreementSerializer(ModelSerializer):
    class Meta:
        model = SpecialistAgreements
        fields = "__all__"


class RegisterSpecialistSerializer(ModelSerializer):
    # personal_information = SpecialistPersonalInfoSerializer()
    # professional_detail = SpecialistProfessionalDetailSerializer()
    # verification_document = SpecialistVerificationDocumentSerializer()
    # agreement = SpecialistAgreementSerializer()
    
    class Meta:
        model = RegisterSpecialist
        fields = "__all__"
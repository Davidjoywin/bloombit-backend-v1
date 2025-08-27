from rest_framework.serializers import ModelSerializer
from django.shortcuts import get_object_or_404

from .models import ClinicalNote, LabResult, Patient, Vital, Allergy, Medication, MedicalCondition, UserProfile


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):
        auth_user_id = self.context['request'].user.id
        user_profile = get_object_or_404(UserProfile, id=auth_user_id)
        validated_data['user'] = user_profile

        patient = Patient.objects.create(**validated_data)
        patient.save()
        return patient


class VitalSerializer(ModelSerializer):
    class Meta:
        model = Vital
        fields = "__all__"

    def create(self, validated_data):
        vital = Vital.objects.create(**validated_data)
        vital.save()
        return vital
    
class AllergySerializer(ModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"

class MedicationSerializer(ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"

class MedicalConditionSerializer(ModelSerializer):
    class Meta:
        model = MedicalCondition
        fields = "__all__"

class LabResultSerializer(ModelSerializer):
    class Meta:
        model = LabResult
        fields = "__all__"

class ClinicalNoteSerializer(ModelSerializer):
    class Meta:
        model = ClinicalNote
        fields = "__all__"


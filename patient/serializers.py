from rest_framework import validators
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

    def validate(self, attrs):
        request = self.context['request']
        user_profile = UserProfile.objects.get(username=request.user.username)
        if user_profile.account_type != 'patient':
            raise validators.ValidationError({"user": "User not a Patient"})
        if Patient.objects.filter(user=user_profile).exists() and request.method == 'POST':
            raise validators.ValidationError({"User": "User already has a patient profile"})
        return attrs

    def create(self, validated_data):
        auth_user = self.context['request'].user
        user_profile = get_object_or_404(UserProfile, username=auth_user.username)
        # validated_data['user'] = user_profile

        patient = Patient.objects.create(user=user_profile, **validated_data)
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


from rest_framework.serializers import ModelSerializer

from .models import Patient, Vital


class PatientSerializer(ModelSerializer):
    class Meta:
        models = Patient
        fields = "__all__"

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        patient.save()
        return patient


class VitalSerializer(ModelSerializer):
    class Meta:
        models = Vital
        fields = "__all__"

    def create(self, validated_data):
        vital = Vital.objects.create(**validated_data)
        vital.save()
        return vital
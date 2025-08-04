from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Specialization, Education, MedicalSpecialist


class SpecializationSerializer(ModelSerializer):
    count = serializers.IntegerField(source='medicalspecialist_set.count', read_only=True)

    class Meta:
        model = Specialization
        fields = "__all__"
        read_only_fields = ["slugged_name", "count"]
    
    def create(self, validated_data):
        name = validated_data.name.lower().split('')
        slug = '-'.join(name)
        validated_data.slugged_name = slug
        specialization = Specialization.object.create(**validated_data)
        return specialization

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "school_name",
            "major",
        ]

    def create(self, validated_data):
        education = Education.objects.create(**validated_data)
        education.save()
        return education

class MedicalSpecialistSerializer(ModelSerializer):
    education = EducationSerializer()
    specialization = SpecializationSerializer(read_only=True)

    class Meta:
        model = MedicalSpecialist
        fields = '__all__'

    def create(self, validated_data):
        medical_specialist = MedicalSpecialist.objects.create(**validated_data)
        medical_specialist.save()
        return medical_specialist
    

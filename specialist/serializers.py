from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Specialization, Education, MedicalSpecialist


class SpecializationSerializer(ModelSerializer):
    # slug = '-'.join(validated_data.get('name', '').lower().split(' '))
    count = serializers.IntegerField(source='medicalspecialist_set.count', read_only=True)
    slugged_name = serializers.SlugField(source='sluggify', read_only=True)

    class Meta:
        model = Specialization
        fields = "__all__"
        read_only_fields = ["slugged_name", "count"]
    
    def create(self, validated_data):
        specialization = Specialization.objects.create(**validated_data)
        specialization.save()
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
    

from rest_framework.serializers import ModelSerializer

from .models import Specialization, MedicalSpecialist


class SpecializationSerializer(ModelSerializer):
    class Meta:
        models = Specialization
        excluded = [
            "slug"
        ]
    
    def create(self, validated_data):
        name = validated_data.name.lower()
        slug = '-'.join(name)
        validated_data.slug = slug
        specialization = Specialization.object.create(**validated_data)
        return specialization
    
class MedicalSpecialistSerializer(ModelSerializer):
    class Meta:
        models = MedicalSpecialist
        fields = '__all__'

    def create(self, validated_data):
        medical_specialist = MedicalSpecialist.objects.create(**validated_data)
        medical_specialist.save()
        return medical_specialist
    

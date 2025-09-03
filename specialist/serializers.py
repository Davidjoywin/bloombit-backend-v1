import json
from rest_framework import serializers, validators
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Specialization, UserProfile, Education, MedicalSpecialist, Language


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
    
class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        exclude = ['medical_specialist']
        extra_kwargs = {"id": {"read_only": True}}

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        exclude = ['medical_specialist']
        read_only_fields = ["id", "medical_specialist"]

    def create(self, validated_data):
        education = Education.objects.create(**validated_data)
        education.save()
        return education

# class MedicalSpecialistSerializer(ModelSerializer):
#     education = EducationSerializer()

#     class Meta:
#         model = MedicalSpecialist
#         fields = '__all__'

#     def create(self, validated_data):
#         medical_specialist = MedicalSpecialist.objects.create(**validated_data)
#         medical_specialist.save()
#         return medical_specialist


class MedicalSpecialistSerializer(ModelSerializer):
    # personal_information = SpecialistPersonalInfoSerializer()
    # professional_details = SpecialistProfessionalDetailSerializer()
    # verification_documents = SpecialistVerificationDocumentSerializer()
    # agreements = SpecialistAgreementSerializer()
    languages = LanguageSerializer(source='language_set', many=True)
    educations = EducationSerializer(source='education_set', many=True)

    
    class Meta:
        model = MedicalSpecialist
        fields = "__all__"
        extra_kwargs = {
            "languages": {"required": False},
            "educations": {"required": False},
            "id": {"required": False, "read_only": True},
            "user": {"required": False, "read_only": True},
        }

    def validate(self, attrs):
        request = self.context['request']
        user = UserProfile.objects.get(username=request.user.username)
        if MedicalSpecialist.objects.filter(user=user).exists() and request.method == 'POST':
            raise validators.ValidationError({"user": "User already has medical specialist profile"})
        if user.account_type != 'specialist':
            raise validators.ValidationError({"User": "User is not a specialist"})
        return attrs

    def create(self, validated_data):
        languages = validated_data.pop('language_set')
        educations = validated_data.pop('education_set')
        user_profile=UserProfile.objects.get(username=self.context['request'].user.username)

        medical_specialist = MedicalSpecialist.objects.create(user=user_profile, **validated_data)
        for language in languages:
            Language.objects.create(medical_specialist=medical_specialist, **language)
        for education in educations:
            Education.objects.create(medical_specialist=medical_specialist, **education)
        return medical_specialist
    
    def update(self, instance, validated_data):
        print("This is the rest level")
        if self.context['request'].method == 'put':
            for key, value in validated_data:
                setattr(instance, key, value)
                instance.save()
            return instance
        return instance
        
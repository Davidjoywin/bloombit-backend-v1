from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

from .utils import create_token
from consult.models import Consultation
from .models import UserProfile, Professional


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "phone_no",
            "account_type"
        ]
    
    def create(self, validated_data):
        account = UserProfile.objects.create(**validated_data)
        account.set_password(validated_data['password'])
        account.save()
        if validated_data['account_type'] == "professional":
            professional = Professional.objects.create(user=account)
            professional.save()
        return account
    
class KPISerializer:
    users = serializers.IntegerField()
    patients = serializers.IntegerField()
    professionals = serializers.IntegerField()
    active_users = serializers.IntegerField()
    non_active_users = serializers.IntegerField()
    total_consultations = serializers.IntegerField()
    completed_consultations = serializers.IntegerField()
    uncompleted_consultations = serializers.IntegerField()

    def __init__(self):
        self.set_data()

    def set_data(self):
        self.users = len(UserProfile.objects.all())
        self.patients = len(UserProfile.objects.filter(account_type='patient'))
        self.professionals = len(UserProfile.objects.filter(account_type='professional'))
        self.active_users = len(UserProfile.objects.filter(is_active=True))
        self.non_active_users = len(UserProfile.objects.filter(is_active=False))
        self.total_consultations = len(Consultation.objects.all())
        self.completed_consultations = len(Consultation.objects.filter(consult_done=True))
        self.uncompleted_consultations = len(Consultation.objects.filter(consult_done=False))
    
    def data(self):
        data = self.__dict__
        return data

class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_no",
            "account_type"
        ]

        extra_kwargs = {
            'username': {"required": False, "read_only": True},
            'password': {"required": False, "read_only": True},
            "email": {"required": False, "read_only": True},
            "phone_number": {"required": False, "read_only": True},
            "account_type": {"read_only": True}
        }
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=25)

    def validate(self, data):
        try:
            user = UserProfile.objects.get(username=data['username'])
        except Exception:
            raise ValidationError({'user': "User not found"})
        if not user.check_password(data['password']):
            raise ValidationError({"password": "Incorrect password"})
        login(self.context['request'], user)
        return data
    
class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = [
            'user',
            'field',
            'summary',
        ]
        extra_kwargs = {
            'user': {'required': False, 'read_only': True},
            'field': {'required': False},
            'summary': {'required': False},
        }

from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

from .models import UserProfile, Professional
from .utils import create_token


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
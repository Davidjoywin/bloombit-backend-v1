from django.contrib.auth import logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..utils import create_token
from ..models import UserProfile
from ..serializers import LoginSerializer, UserProfileSerializer

class Auth(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = UserProfile.objects.get(username=serializer.validated_data['username'])
            user_serializer = UserProfileSerializer(user, context={'request': request})
            token = create_token(user)
            return Response(
                {
                    'status': True,
                    'message': "Login successfully",
                    'user': user_serializer.data,
                    'token': token,
                    'statusCode': status.HTTP_200_OK
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status': False,
                'message': "Login failed",
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
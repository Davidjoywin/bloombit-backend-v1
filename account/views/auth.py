from django.contrib.auth import logout
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser

from django.contrib.auth import login

from ..utils import create_token
from ..models import UserProfile
from ..serializers import LoginSerializer, UserProfileSerializer

class Auth(APIView):
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]
    serializer_class = LoginSerializer

    @extend_schema(
        request=LoginSerializer,
        responses={200: UserProfileSerializer, 400: {"message": "Login failed"}}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        if serializer.is_valid():
            try:
                user = UserProfile.objects.get(username=serializer.validated_data['username'])
                if not user.check_password(serializer.validated_data.get('password', '')):
                    return Response(
                        {
                            'status': False,
                            'message': "Login failed",
                            'error': {'password': ['Incorrect password']},
                            'statusCode': status.HTTP_400_BAD_REQUEST
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                login(request, user)
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
            except:
                return Response(
                    {
                        'status': False,
                        'message': "Login Failed",
                        'error': {'username': ['User not found']},
                        'statusCode': status.HTTP_400_BAD_REQUEST
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {
                'status': False,
                'message': "Login failed",
                'errors': serializer.errors,
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
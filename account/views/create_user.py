from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..utils import create_token
from ..models import UserProfile
from ..serializers import UserProfileSerializer


class CreateUser(APIView):

    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            user = UserProfile.objects.get(username=serializer.validated_data['username'])
            token = create_token(user)
            return Response(
                {
                    "status": True,
                    "data": serializer.data,
                    "token": token,
                    "message": "User created successfully",
                    "statusCode": status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'status': False,
                'data': serializer.errors,
                'message': "User failed to create",
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )

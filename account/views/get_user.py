from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import UserProfile
from ..permissions import IsAuthenticatiedUserOrReadOnlyd
from ..serializers import UserProfileSerializer, UpdateUserSerializer


class GetUser(APIView):
    permission_classes = [IsAuthenticatiedUserOrReadOnlyd]
    def get_object(self, pk):
        obj = get_object_or_404(UserProfile, pk=pk)
        return obj
        
    def get(self, request, id):
        user = self.get_object(pk=id)
        self.check_object_permissions(request, user)
        serializer = UserProfileSerializer(user, context={"request": request})
        return Response(
            {
                'status': True,
                'message': "User successfully retrieved",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
    
    def put(self, request, id):
        user = self.get_object(id)
        self.check_object_permissions(request, user)
        serializer = UpdateUserSerializer(user, data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'status': True,
                    'message': "User updated successfully",
                    'data': serializer.data,
                    'statusCode': status.HTTP_200_OK
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status': False,
                'message': "User update failed",
                'data': serializer.errors,
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import UserProfile, Professional
from ..serializers import ProfessionalSerializer
from ..permissions import IsAuthenticatiedUserOrReadOnlyd


class GetProfessional(APIView):
    permission_classes = [IsAuthenticatiedUserOrReadOnlyd]

    def get_objects(self, id):
        user = get_object_or_404(UserProfile, pk=id)
        professional = get_object_or_404(Professional, user=user)
        return [user, professional]

    def get(self, request, id):
        user, professional = self.get_objects(id)
        self.check_object_permissions(request, user)
        serializer = ProfessionalSerializer(professional, context={'request': request})
        return Response(
            {
                'status': True,
                'message': "Professial profile retrieved successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
    
    def put(self, request, id):
        user, professional = self.get_objects(id)
        self.check_object_permissions(request, user)
        serializer = ProfessionalSerializer(professional, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': True,
                    'message': "Professional profile updated",
                    'data': serializer.data,
                    'statusCode': status.HTTP_200_OK
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
            {
                'status': False, 
                'message': "Professional profile update failed",
                'data': serializer.errors,
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from ..serializers import RegisterSpecialistSerializer


class RegisterSpecialist(APIView):
    
    def post(self, request):
        serializer = RegisterSpecialistSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                    "status": True,
                    "data": serializer.data,
                    "statusCode": status.HTTP_200_OK,
                    "message": "Specialist Created Successfully"
            }, content_type="multipart/form-data", status=status.HTTP_200_OK)
        return Response({
            "status": False,
            "data": serializer.errors,
            "statusCode": status.HTTP_400_BAD_REQUEST,
            "message": "Failed to create a specialist"
        }, content_type="multipart/form-data", status=status.HTTP_400_BAD_REQUEST)
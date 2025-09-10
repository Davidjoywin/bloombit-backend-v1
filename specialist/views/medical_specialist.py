import json
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from drf_spectacular.utils import extend_schema

from ..models import MedicalSpecialist, Specialization
from ..serializers import MedicalSpecialistSerializer, MedicalSpecialistWithDetailedCategorySerializer


class CreateMedicalSpecialist(APIView):

    serializer_class = MedicalSpecialistSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        request_data = request.data
        validated_data = {key: value for key, value in request_data.items()}
        validated_data['languages'] = json.loads(request_data.get('languages', '[]'))
        validated_data['educations'] = json.loads(request_data.get('educations', '[]'))

        serializer = MedicalSpecialistSerializer(data=validated_data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                    "status": True,
                    "data": serializer.data,
                    "statusCode": status.HTTP_200_OK,
                    "message": "Specialist Created Successfully"
            }, status=status.HTTP_200_OK)
        return Response({
            "status": False,
            "error": serializer.errors,
            "statusCode": status.HTTP_400_BAD_REQUEST,
            "message": "Failed to create a specialist"
        }, status=status.HTTP_400_BAD_REQUEST)


class MedicalSpecialistView(APIView):

    parser_classes = [MultiPartParser, FormParser]
    serializer_class = MedicalSpecialistSerializer

    @extend_schema(
        description="Retrieve a medical specialist by ID",
        summary="Retrieve Medical Specialist by ID"
    )
    def get(self, request, id):
        medical_specialist = get_object_or_404(MedicalSpecialist, id=id)
        serializer = self.serializer_class(medical_specialist, many=False)
        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=serializer_class,
        description="Update a medical specialist by ID",
        summary="Update Medical Specialist"
    )
    def put(self, request, id):
        medical_specialist = get_object_or_404(MedicalSpecialist, id=id)
        request_data = request.data
        validated_data = {key: value for key, value in request_data.items()}
        
        validated_data['languages'] = json.loads(request_data.get('languages', ''))
        validated_data['educations'] = json.loads(request_data.get('educations', '[]'))
        # print(validated_data)
        serializer = MedicalSpecialistSerializer(medical_specialist, data=validated_data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "success",
                "data": serializer.data,
                "statusCode": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': True,
            'message': "failed",
            'data': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        description="Delete a medical specialist by ID",
        summary="Delete Medical Specialist"
    )
    def delete(self, request, id):
        medical_specialist = get_object_or_404(MedicalSpecialist, id=id)
        medical_specialist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalSpecialistByCategoryView(APIView):
    serializer_class = MedicalSpecialistWithDetailedCategorySerializer

    @extend_schema(
        description="Retrieve medical specialists by specialization slugged_name",
        summary="Retrieve Medical Specialists by Specialization"
    )
    def get(self, request, slugged_name):
        # specialization = get_object_or_404(Specialization, slugged_name=slugged_name)
        # specialization = Specialization.objects.first()
        medical_specialists = MedicalSpecialist.objects.filter(specialization__slugged_name=slugged_name)
        serializer = self.serializer_class(medical_specialists, many=True)
        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
        
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
    
class AllMedicalSpecialistView(APIView):
    # serializer_class = MedicalSpecialistSerializer
    pagination_class = StandardResultsSetPagination
    serializer_class = MedicalSpecialistWithDetailedCategorySerializer

    @extend_schema(
        description="Retrieve all medical specialists",
        summary="Retrieve All Medical Specialists"
    )
    def get(self, request):
        medical_specialists = MedicalSpecialist.objects.all()
        serializer = self.serializer_class(medical_specialists, many=True)
        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
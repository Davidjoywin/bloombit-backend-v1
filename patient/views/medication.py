from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema

from ..models import Medication
from ..serializers import PatientSerializer


class CreateMedicationView(APIView):
    serializer_class = PatientSerializer
    parser_classes = [JSONParser]

    @extend_schema(
        request=serializer_class
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Medication created successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Medication creation failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetMedicationView(APIView):
    serializer_class = PatientSerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            medication = Medication.objects.get(id=id)
        except Medication.DoesNotExist:
            return Response({
                'status': False,
                'message': "Medication not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(medication)
        return Response({
            'status': True,
            'message': "Medication retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=serializer_class
    )
    def put(self, request, id):
        try:
            medication = Medication.objects.get(id=id)
        except Medication.DoesNotExist:
            return Response({
                'status': False,
                'message': "Medication not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(medication, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Medication updated successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "Medication update failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class ListMedicationsView(APIView):
    serializer_class = PatientSerializer

    def get(self, request):
        medications = Medication.objects.all()
        serializer = self.serializer_class(medications, many=True)
        return Response({
            'status': True,
            'message': "Medications retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

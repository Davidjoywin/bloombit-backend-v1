from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema

from ..models import MedicalCondition
from ..serializers import MedicalConditionSerializer


class CreateMedicalConditionView(APIView):
    serializer_class = MedicalConditionSerializer
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
                'message': "Medical condition created successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Medical condition creation failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetMedicalConditionView(APIView):
    serializer_class = MedicalConditionSerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            medical_condition = MedicalCondition.objects.get(id=id)
        except MedicalCondition.DoesNotExist:
            return Response({
                'status': False,
                'message': "Medical condition not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(medical_condition)
        return Response({
            'status': True,
            'message': "Medical condition retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

    @extend_schema(
        request=serializer_class
    )
    def put(self, request, id):
        try:
            medical_condition = MedicalCondition.objects.get(id=id)
        except MedicalCondition.DoesNotExist:
            return Response({
                'status': False,
                'message': "Medical condition not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(medical_condition, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Medical condition updated successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "Medical condition update failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetPatientMedicalConditions(APIView):
    serializer_class = MedicalConditionSerializer

    def get(self, request, patient_id):
        try:
            clinical_note = MedicalCondition.objects.get(patient_id=patient_id)
        except:
            return Response({
                'status': False,
                'message': "No medical condition was found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(clinical_note, many=True)
        return Response({
            'status': True,
            'message': "Retrieved medical conditions for patient successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
class ListMedicalConditionsView(APIView):
    serializer_class = MedicalConditionSerializer

    def get(self, request):
        medical_conditions = MedicalCondition.objects.all()
        serializer = self.serializer_class(medical_conditions, many=True)
        return Response({
            'status': True,
            'message': "Medical conditions retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
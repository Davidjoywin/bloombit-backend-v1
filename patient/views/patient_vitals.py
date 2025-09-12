from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from django.shortcuts import get_object_or_404

from ..serializers import VitalSerializer
from ..models import Patient, Vital, UserProfile


class CreatePatientVitals(APIView):
    serializer_class = VitalSerializer
    permission_classes = [IsAuthenticated]
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
                'message': 'Vital signs recorded successfully',
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Vital sign recording failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class AuthPatientVitals(APIView):

    serializer_class = VitalSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        auth_user = request.user
        user_profile = UserProfile.objects.get(username=auth_user.username)
        patient = get_object_or_404(Patient, user=user_profile)
        vitals = patient.vital_set.all()
        serializer = VitalSerializer(vitals, many=True)
        return Response({
            'status': True,
            'message': "success",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

class GetPatientVital(APIView):

    parser_classes = [JSONParser]
    serializer_class = VitalSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, vital_id):
        auth_user_id = request.user.id
        patient = get_object_or_404(Patient, id=auth_user_id)
        vital = get_object_or_404(Vital, id=vital_id, patient=patient)
        serializer = VitalSerializer(vital, many=False)
        return Response({
            'status': True,
            'message': "success",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

    @extend_schema(
        request=serializer_class
    )
    def put(self, request, vital_id):
        auth_user_id = request.user.id
        patient = get_object_or_404(Patient, id=auth_user_id)
        vital = get_object_or_404(Vital, id=vital_id, patient=patient)

        serializer = VitalSerializer(vital, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "success",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, vital_id):
        auth_user_id = request.user.id
        patient = get_object_or_404(Patient, id=auth_user_id)
        vital = get_object_or_404(Vital, id=vital_id, patient=patient)
        vital.delete()
        return Response({
            'status': True,
            'message': "Vital sign deleted successfully",
            'statusCode': status.HTTP_204_NO_CONTENT
        }, status=status.HTTP_204_NO_CONTENT)
    
class GetPatientVitals(APIView):

    serializer_class = VitalSerializer

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, id=patient_id)
        vitals = patient.vital_set.all()
        serializer = VitalSerializer(vitals, many=True)
        return Response({
            'status': True,
            'message': "success",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
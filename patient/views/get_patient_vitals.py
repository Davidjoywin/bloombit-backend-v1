from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Patient, Vital
from ..serializers import VitalSerializer


class AuthPatientVitals(APIView):
    def get(self, request):
        auth_user_id = request.user.id
        patient = get_object_or_404(Patient, id=auth_user_id)
        vitals = patient.vital_set.all()
        serializer = VitalSerializer(vitals, many=True)
        return Response({
            'status': True,
            'message': "success",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

class GetPatientVitals(APIView):
    def get(self, request, id):
        patient = get_object_or_404(Patient, id=id)
        vitals = patient.vital_set.all()
        serializer = VitalSerializer(vitals, many=True)
        return Response({
            'status': True,
            'message': "success",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

   
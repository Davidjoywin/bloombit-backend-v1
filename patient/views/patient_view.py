from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from ..models import Patient, UserProfile
from ..serializers import PatientSerializer


class CreatePatient(APIView):
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
                'message': "Patient created successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Patient creation failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class AuthPatientView(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer

    def get(self, request):
        auth_user_id = request.user.id
        print(auth_user_id)
        user_profile = UserProfile.objects.get(id=auth_user_id)
        print(user_profile.account_type)
        if user_profile.account_type == 'patient':
            patient = user_profile.patient
            serializer = PatientSerializer(patient, many=False)
            return Response({
                'status': True,
                'message': "Patient retrieved successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "User account type should be patient",
            'statusCode': status.HTTP_307_TEMPORARY_REDIRECT
        }, status=status.HTTP_307_TEMPORARY_REDIRECT)
    
class GetPatientView(APIView):
    serializer_class = PatientSerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            return Response({
                'status': False,
                'message': "Patient not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(patient)
        return Response({
            'status': True,
            'message': "Patient retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=serializer_class
    )
    def put(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            return Response({
                'status': False,
                'message': "Patient not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(patient, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Patient updated successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "Patient update failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            patient = Patient.objects.get(id=id)
            patient.delete()
            return Response({
                'status': True,
                'message': "Patient profile deleted successfully",
                'statusCode': status.HTTP_204_NO_CONTENT
            }, status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response({
                'status': False,
                'message': "Patient not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
    
class ListPatientsView(APIView):
    serializer_class = PatientSerializer

    def get(self, request):
        patients = Patient.objects.all()
        serializer = self.serializer_class(patients, many=True)
        return Response({
            'status': True,
            'message': "Patients retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
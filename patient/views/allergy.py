from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from ..models import Patient, Allergy
from ..serializers import AllergySerializer


class CreateAllergyView(APIView):
    serializer_class = AllergySerializer
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
                'message': "Allergy created successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Allergy creation failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)


class GetAllergyView(APIView):
    serializer_class = AllergySerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            auth_user_id = request.user.id
            patient = Patient.objects.get(user__id=auth_user_id)
            allergy = Allergy.objects.get(id=id, patient=patient)
        except Allergy.DoesNotExist:
            return Response({
                'status': False,
                'message': "Allergy not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(allergy)
        return Response({
            'status': True,
            'message': "Allergy retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

    @extend_schema(
        request=serializer_class
    )
    def put(self, request, id):
        try:
            allergy = Allergy.objects.get(id=id)
        except Allergy.DoesNotExist:
            return Response({
                'status': False,
                'message': "Allergy not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(allergy, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Allergy updated successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "Allergy update failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class ListAllergiesView(APIView):
    serializer_class = AllergySerializer

    def get(self, request):
        auth_user_id = request.user.id
        patient = get_object_or_404(Patient, user__id=auth_user_id)
        allergies = Allergy.objects.filter(patient=patient)
        serializer = self.serializer_class(allergies, many=True)
        return Response({
            'status': True,
            'message': "Allergies retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
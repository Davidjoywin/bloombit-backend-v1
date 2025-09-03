from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema

from ..models import ClinicalNote
from ..serializers import ClinicalNoteSerializer

class CreateClinicalNoteView(APIView):
    serializer_class = ClinicalNoteSerializer
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
                'message': "Clinical note created successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Clinical note creation failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetClinicalNoteView(APIView):
    serializer_class = ClinicalNoteSerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            clinical_note = ClinicalNote.objects.get(id=id)
        except ClinicalNote.DoesNotExist:
            return Response({
                'status': False,
                'message': "Clinical note not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(clinical_note)
        return Response({
            'status': True,
            'message': "Clinical note retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=serializer_class
    )
    def put(self, request, id):
        try:
            clinical_note = ClinicalNote.objects.get(id=id)
        except ClinicalNote.DoesNotExist:
            return Response({
                'status': False,
                'message': "Clinical note not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(clinical_note, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Clinical note updated successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "Clinical note update failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetPatientClinicalNotes(APIView):
    serializer_class = ClinicalNoteSerializer

    def get(self, request, patient_id):
        try:
            clinical_note = ClinicalNote.objects.get(patient_id=patient_id)
        except:
            return Response({
                'status': False,
                'message': "No Clinal Note was found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(clinical_note, many=True)
        return Response({
            'status': True,
            'message': "Retrieved Clinical notes for patient successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
class ListClinicalNotesView(APIView):
    serializer_class = ClinicalNoteSerializer

    def get(self, request):
        clinical_notes = ClinicalNote.objects.all()
        serializer = self.serializer_class(clinical_notes, many=True)
        return Response({
            'status': True,
            'message': "Clinical notes retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
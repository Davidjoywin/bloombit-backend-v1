from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema

from ..models import LabResult
from ..serializers import LabResultSerializer


class CreateLabResultView(APIView):
    serializer_class = LabResultSerializer
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
                'message': "Lab result created successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "Lab result creation failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetLabResultView(APIView):
    serializer_class = LabResultSerializer
    parser_classes = [JSONParser]

    def get(self, request, id):
        try:
            lab_result = LabResult.objects.get(id=id)
        except LabResult.DoesNotExist:
            return Response({
                'status': False,
                'message': "Lab result not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(lab_result)
        return Response({
            'status': True,
            'message': "Lab result retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=serializer_class
    )
    def put(self, request, id):
        try:
            lab_result = LabResult.objects.get(id=id)
        except LabResult.DoesNotExist:
            return Response({
                'status': False,
                'message': "Lab result not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(lab_result, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Lab result updated successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': "Lab result update failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
class GetPatientLabResults(APIView):
    serializer_class = LabResultSerializer

    def get(self, request, patient_id):
        try:
            lab_result = LabResult.objects.get(patient_id=patient_id)
        except:
            return Response({
                'status': False,
                'message': "No Lab Result was found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(lab_result, many=True)
        return Response({
            'status': True,
            'message': "Retrieved lab results for patient successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
class ListLabResultsView(APIView):
    serializer_class = LabResultSerializer

    def get(self, request):
        lab_results = LabResult.objects.all()
        serializer = self.serializer_class(lab_results, many=True)
        return Response({
            'status': True,
            'message': "Lab results retrieved successfully",
            'data': serializer.data,
            'statusCode': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

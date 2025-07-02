from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from ..serializers import VitalSerializer

class PatientVitals(ModelSerializer):
    def post(self, request, id):
        # patient = get_object_or_404(Patient, id=id)
        serializer = VitalSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success',
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "success",
            'data': serializer.error,
            'statusCode': status.HTTP_400_BAD_REQUEST
    
        }, status=status.HTTP_400_BAD_REQUEST)
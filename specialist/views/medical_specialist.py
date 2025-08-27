from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import MedicalSpecialist, Specialization
from ..serializers import MedicalSpecialistSerializer


class CreateMedicalSpecialist(APIView):
    serializer_class = MedicalSpecialistSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "success",
                'data': serializer.data,
                'statusCode': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': "failed",
            'error': serializer.errors,
            'statusCode': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    

class MedicalSpecialistView(APIView):

    def get(self, request, id):
        medical_specialist = get_object_or_404(MedicalSpecialist, id=id)
        serializer = self.serializer_class(medical_specialist, many=False)
        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        medical_specialist = get_object_or_404(MedicalSpecialist, id=id)
        serializer = MedicalSpecialistSerializer(medical_specialist, data=request.data, context={"request": request})
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
    
    def delete(self, request, id):
        medical_specialist = get_object_or_404(MedicalSpecialist, id=id)
        medical_specialist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalSpecialistByCategoryView(APIView):
    serializer_class = MedicalSpecialistSerializer

    def get(self, request, slugged_name):
        specialization = get_object_or_404(Specialization, slugged_name=slugged_name)
        medical_specialists = MedicalSpecialist.objects.filter(specialization=specialization)
        serializer = self.serializer_class(medical_specialists, many=True)
        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
class AllMedicalSpecialistView(APIView):
    serializer_class = MedicalSpecialistSerializer

    def get(self, request, id):
        medical_specialists = MedicalSpecialist.objects.all()
        serializer = self.serializer_class(medical_specialists, many=True)
        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Specialization
from ..serializers import SpecializationSerializer


class GetCategories(APIView):
    def get(self):
        specialization = Specialization.objects.all()
        serializer = SpecializationSerializer(specialization, many=True)
        return Response({
                "status": True,
                "message": "Retrived medical Specialization Successfully",
                "data": serializer.data,
                "statusCode": status.HTTP_200_OK
            }, status=True
        )
    
class Category(APIView):
    def get(self, request, slug):
        specialization = get_object_or_404(Specialization, slug=slug)
        serializer = SpecializationSerializer(specialization, many=False)

        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK        
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SpecializationSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": True,
                "message": "created",
                "data": serializer.data,
                "statusCode": status.HTTP_201_CREATED
            },status=status.HTTP_200_OK)
        return Response({
            "status": True,
            "message": "failed",
            "error": serializer.errors,
            "statusCode": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, slug):
        specialization = get_object_or_404(Specialization, slug=slug)
        serializer = SpecializationSerializer(specialization, data=request.data, content={"request": request})
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": True,
                "message": "success",
                "statusCode": status.HTTP_202_ACCEPTED
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
            "status": False,
            "message": "failed",
            "statusCode": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, slug):
        specialization = get_object_or_404(Specialization, slug=slug)
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
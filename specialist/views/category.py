from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema

from ..models import Specialization
from ..serializers import SpecializationSerializer


class GetCategories(APIView):

    serializer_class = SpecializationSerializer

    @extend_schema(
        description="Retrieve all medical specializations",
        summary="Retrieve all medical specializations"
    )
    def get(self, request):
        specialization = Specialization.objects.all()
        serializer = self.serializer_class(specialization, many=True)
        # print(serializer.data)
        return Response({
                "status": True,
                "message": "Retrived medical Specialization Successfully",
                "data": serializer.data,
                "statusCode": status.HTTP_200_OK
            }, status=status.HTTP_200_OK
        )
    
class CreateCategory(APIView):
    parser_classes = [JSONParser]
    serializer_class = SpecializationSerializer

    @extend_schema(
        request=serializer_class,
        description="Create a new specialization",
        summary="Create Specialization"
    )
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
    
class Category(APIView):
    parser_classes = [JSONParser]
    serializer_class = SpecializationSerializer

    @extend_schema(
        description="Retrieve, update or delete a specialization by slugged_name",
        summary="Retrieve, update or delete Specialization"
    )
    def get(self, request, id):
        specialization = get_object_or_404(Specialization, id=id)
        serializer = self.serializer_class(specialization, many=False)

        return Response({
            "status": True,
            "message": "success",
            "data": serializer.data,
            "statusCode": status.HTTP_200_OK        
        }, status=status.HTTP_200_OK)
    
    @extend_schema(
        request=serializer_class,
        description="Update a specialization by slug",
        summary="Update Specialization"
    )
    def put(self, request, id):
        specialization = get_object_or_404(Specialization, id=id)
        serializer = SpecializationSerializer(specialization, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": True,
                "data": serializer.data,
                "message": "success",
                "statusCode": status.HTTP_202_ACCEPTED
            }, status=status.HTTP_202_ACCEPTED)
        return Response({
            "status": False,
            "error": serializer.errors,
            "message": "failed",
            "statusCode": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        description="Delete a specialization by slug",
        summary="Delete Specialization"
    )
    def delete(self, request, id):
        specialization = get_object_or_404(Specialization, id=id)
        specialization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
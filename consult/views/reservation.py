from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Consultation
from account.models import UserProfile
from ..permissions import IsAuthenticatedOrOwner
from ..serializers import ConsultationSerializer


class Reservation(APIView):

    permission_classes = [IsAuthenticatedOrOwner]

    def get_object(self, id):
        consult_obj = get_object_or_404(Consultation, id=id)
        return consult_obj

    def get(self, request, id):
        reservation = self.get_object(id)
        self.check_object_permissions(request, reservation)
        reservation_serializer = ConsultationSerializer(reservation, context={'request': request})
        return Response(
            {
                'status': True,
                'message': "Reservation retrieved successfully",
                'data': reservation_serializer.data,
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
    
    def put(self, request, id):
        reservation = self.get_object(id)
        self.check_object_permissions(request, reservation)
        reservation_serializer = ConsultationSerializer(reservation, data=request.data, context={"request": request})
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return Response(
                {
                    'status': True,
                    'message': "Reservation updated successfully",
                    'data': reservation_serializer.data,
                    'statusCode': status.HTTP_200_OK
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status': False,
                'message': "Reservation failed to update",
                'data': reservation_serializer.data,
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
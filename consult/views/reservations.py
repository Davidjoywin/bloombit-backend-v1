from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Consultation
from account.models import UserProfile
from ..serializers import ConsultationSerializer


class UserReservations(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        self.check_object_permissions(request, user)
        # auth_user_reservation = Consultation.objects.filter(patient=user)
        print(user)
        reservation = Consultation.objects.filter(patient=user)
        serializer = ConsultationSerializer(reservation, context={'request': request}, many=True)
        return Response(
            {
                'status': True,
                'message': "Authenticated User Reservations retrieved successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
    
class Reservations(APIView):

    def get(self, request):
        reservation = Consultation.objects.all()
        serializer = ConsultationSerializer(reservation, context={'request': request}, many=True)
        return Response(
            {
                'status': True,
                'message': "Reservations for patient retrieved successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
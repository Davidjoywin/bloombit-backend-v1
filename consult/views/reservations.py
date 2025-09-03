from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Consultation
from patient.models import Patient
from account.models import UserProfile
from ..serializers import ConsultationSerializer


class UserReservations(APIView):

    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        self.check_object_permissions(request, user)
        # auth_user_reservation = Consultation.objects.filter(patient=user)
        try:
            user_profile = UserProfile.objects.get(username=user.username)
            patient = Patient.objects.get(user=user_profile)
        except:
            return Response({
                'status': False,
                'message': "Patient profile not found",
                'statusCode': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        reservation = Consultation.objects.filter(patient=patient)
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
    serializer_class = ConsultationSerializer

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
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Consultation
from ..serializers import ConsultationSerializer


class Reservations(APIView):

    def get(self, request):
        auth_user_reservation = Consultation.objects.filter(id=request.user.id)
        serializer = ConsultationSerializer(auth_user_reservation, data=request.data, context={'request': request}, many=True)
        return Response(
            {
                'status': True,
                'message': "Reservations for patient retrieved successfully",
                'data': serializer.data,
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
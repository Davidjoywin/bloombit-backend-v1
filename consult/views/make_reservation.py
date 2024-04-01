from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import ConsultationSerializer
from ..permissions import IsAuthenticatedOrOwner


class MakeReservation(APIView):

    def post(self, request):
        serializer = ConsultationSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': True,
                    'message': "Reservation made successfully",
                    'data': serializer.data,
                    'statusCode': status.HTTP_201_CREATED
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'status': False,
                'message': "Reservation failed",
                'data': serializer.errors,
                'statusCode': status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )
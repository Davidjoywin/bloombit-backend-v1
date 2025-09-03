from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from drf_spectacular.utils import extend_schema

from ..permissions import IsAuthenticatedOrOwner
from ..serializers import MakeReservationSerializer


class MakeReservation(APIView):
    parser_classes = [JSONParser]
    serializer_class = MakeReservationSerializer
    permission_classes = [IsAuthenticatedOrOwner]

    @extend_schema(
        request=MakeReservationSerializer
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})

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
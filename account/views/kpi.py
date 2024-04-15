import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from ..serializers import KPISerializer


class KPI(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        
        serializer = KPISerializer()

        return Response(
            {
                'status': True,
                'message': "KPI retrieved successfully",
                'data': serializer.data(),
                'statusCode': status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
        )
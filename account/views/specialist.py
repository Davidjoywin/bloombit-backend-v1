import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from ..serializers import RegisterSpecialistSerializer


class RegisterSpecialist(APIView):

    serializer_class = RegisterSpecialistSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        personal_information = json.loads(request.data.get("personal_information", {}))
        professional_details = json.loads(request.data.get("professional_details", {}))
        verification_documents = json.loads(request.data.get("verification_documents", {}))
        agreements = json.loads(request.data.get("agreements", {}))
        verification_documents['profile_photo'] = request.data.get("profile_photo")
        verification_documents["government_issued_id"] = request.data.get("government_issued_id")
        verification_documents["medical_license"] = request.data.get("medical_license")
        verification_documents["medical_degree_certificate"] = request.data.get("medical_degree_certificate")
        verification_documents["additional_certificate"] = request.data.get("additional_certificate")
        new_data = {**personal_information, **professional_details, **verification_documents, **agreements}
        serializer = RegisterSpecialistSerializer(data=new_data)
        if serializer.is_valid():
            return Response({
                    "status": True,
                    "data": serializer.data,
                    "statusCode": status.HTTP_200_OK,
                    "message": "Specialist Created Successfully"
            }, content_type="multipart/form-data", status=status.HTTP_200_OK)
        return Response({
            "status": False,
            "data": serializer.errors,
            "statusCode": status.HTTP_400_BAD_REQUEST,
            "message": "Failed to create a specialist"
        }, content_type="multipart/form-data", status=status.HTTP_400_BAD_REQUEST)
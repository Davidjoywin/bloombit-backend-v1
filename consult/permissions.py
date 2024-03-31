from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from .models import Consultation


class IsAuthenticatedOrOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(view)

        return (request.user.id == obj.patient.id)
    
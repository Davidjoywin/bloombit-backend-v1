from rest_framework import permissions


class IsAuthenticatiedUserOrReadOnlyd(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (
            (request.user.id == obj.id) or
            (obj.is_superuser or obj.is_staff)
        )
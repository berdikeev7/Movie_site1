from rest_framework.permissions import BasePermission


class CheckRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'pro'


class CheckStatus(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'pro':
            return True
        elif request.user.status == 'simple' and obj.status_movie == 'simple':
            return True
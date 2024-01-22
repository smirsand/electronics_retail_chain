from rest_framework.permissions import BasePermission


class IsNotSuperuser(BasePermission):
    """
    Запрет редактирования если не суперпользователь.
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return request.method in ['HEAD', 'PUT', 'PATCH', 'DELETE']
        return False

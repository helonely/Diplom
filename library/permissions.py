from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Проверка, является ли пользователь Библиотекарем"""
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Moderator').exists()

from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthorEditNote(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # читать публичную заметку может любой авторизированный пользователь
            return True
        return request.user == obj.author  # Вносить изменения в заметку может только автор заметки


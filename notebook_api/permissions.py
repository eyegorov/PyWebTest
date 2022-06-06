from rest_framework.permissions import BasePermission, SAFE_METHODS


class OnlyAuthorEditNote(BasePermission):
    """Класс для отделения прав авторов заметки от авторизированных пользователей"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # читать публичную заметку может любой авторизированный пользователь
            return True
        return request.user == obj.author  # Вносить изменения в заметку может только автор заметки


class OnlyAuthorViewNonPublicNote(BasePermission):
    """Класс, ограничивающий права пользователей - автор не может прочитать чужую непубличную запись"""

    def has_object_permission(self, request, view, obj):
        if obj.author_id != request.user.id:
            return obj.public is True
        return True

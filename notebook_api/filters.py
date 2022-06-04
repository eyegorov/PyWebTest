from django_filters import rest_framework as filters

from notebook.models import Note


class NoteFilter(filters.FilterSet):
    """Класс для фильтрации заметок"""

    class Meta:
        model = Note
        fields = ['note_status', 'importance_status', 'public_status']  # from notebook/models.py

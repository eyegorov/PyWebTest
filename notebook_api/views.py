from django.db.models import Q  # Q объект (django.db.models.Q) - это объект, используемый для инкапсуляции набора
# ключевых аргументов
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from notebook.models import Note
from notebook_api import filters, permissions, serializers


class NoteListCreateAPIView(generics.ListCreateAPIView):
    """Класс  вывода списка заметок и создания заметки"""
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filters = filters.NoteFilter

    def get_queryset(self):
        """Метод, который позволяет автору смотреть свои заметки или заметки других авторов, помеченные как public"""
        queryset = super().get_queryset()
        return queryset.filter(Q(author_at=self.request.user) & Q(public_status=True))  # Заметки этого author или
        # заметки статуса public

    def perform_create(self, serializer):
        """Метод для сохранения созданой заметки за автором"""
        serializer.save(author_at=self.request.user)
        return serializer


class NoteDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Класс представления для вывода данных о конкретной заметке, ее изменения и удаления"""
    permission_classes = [IsAuthenticated & permissions.OnlyAuthorEditNote & permissions.OnlyAuthorViewNonPublicNote]
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer


class PublicNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public_status=True)

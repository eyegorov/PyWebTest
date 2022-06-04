from datetime import datetime

from rest_framework import serializers

from notebook.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Класс сериализации заметок"""

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('create_at',)

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        create_at = datetime.strptime(ret['create_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        update_at = datetime.strptime(ret['update_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # Конвертируем дату в строку в новом формате
        ret['create_at'] = create_at.strftime('%d %B %Y %H:%M:%S')
        ret['update_at'] = update_at.strftime('%d %B %Y %H:%M:%S')
        return ret

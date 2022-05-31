from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _  # Осуществляет перевод заголовков на анг язык


class Note(models.Model):
    """ """

    class Status(models.IntegerChoices):
        """"Класс Product описывает отдельно взятый товар и его характеристики
           :param ACTIVE: статус Активно
           :param POSTPONED: статус Активно
           :param COMPLETED: статус Завершено """

        ACTIVE = 0, _("Активно")
        POSTPONED = 1, _("Отложено")
        COMPLETED = 2, _("Завершено")

    title = models.CharField(max_length=250, verbose_name=_("Наименование заметки"))
    note = models.TextField(max_length=10000, verbose_name=_("Содержание заметки"))
    note_status = models.IntegerField(default=Status.ACTIVE, choices=Status.ACTIVE, verbose_name=_("Статус"))
    important_status = models.BooleanField(default=False, verbose_name=_("Важно"))
    public = models.BooleanField(default=False, verbose_name=_("Важно"))
    create_at = models.DateField(auto_now=True, verbose_name=_("Время создания заметки"))
    update_at = models.DateField(auto_now_add=True, verbose_name=_("Время обновления заметки"))  # ок
    author_at = models.ForeignKey(get_user_model(),
                                  on_delete=models.CASCADE, verbose_name=_("Автор"))

    def date_time_plus(self) -> datetime:
        """ Метод, возвращающий время + 1 день от текущего согласно ТЗ - Эталонный обьект datetime.now() (текущее время)
         плюс созданный объект времени (+ 1 день) """
        return datetime.now() + timedelta(days=1)  # https://pythonist.ru/kak-ispolzovat-obekt-timedelta-
        # dlya-raboty-s-datami-v-python/

    def __str__(self):
        return f"Заметка№{self.id}"

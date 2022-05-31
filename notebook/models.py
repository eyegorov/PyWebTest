# from django.db import models
# from django.db import models
# from django.utils.translation import gettext_lazy as _  # Осуществляет перевод заголовков на анг язык
#
#
# class Note(models.Model):
#     title = models.CharField(max_length=250, verbose_name=_("Наименование заметки"))
#     message = models.TextField(max_length=10000, verbose_name=_("Текст заметки"))
#     public = models.BooleanField(default=False, verbose_name=_("Опубликовать"))
#     create_at = models.DateField(auto_now=True, verbose_name=_("Время создания"))
#     update_at = models.DateField(auto_now_add=True, verbose_name=_("Время обновления")) #ок
#     author_at = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Запись №{self.id}"

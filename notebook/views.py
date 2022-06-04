from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from PyWebTest.local_settings import SERVER_VERSION  # Текущая версия сервера


class IndexView(View):
    def get(self, request):
        return render(request, "notebook/index.html")


class AboutView(View):  # нет возможности оттестировать на ошибки
    def get(self, request):
        template_name = "notebook/version.html"
        context = {
            "server_version": SERVER_VERSION,  # информация о текущей версии сервера
            "user_name": request.user  # информация о текущем пользователе
        }
        return render(
            request,
            template_name=template_name,
            context=context)


class AboutTemplateView(TemplateView):  # есть возможность оттестировать на ошибки
    template_name = "notebook/version.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = SERVER_VERSION
        return context

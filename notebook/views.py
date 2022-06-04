from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

SERVER_VERSION = "0.0.1"  # Информация о текущей версии сайта


class IndexView(View):
    def get(self, request):
        return render(request, "notebook/index.html")


class AboutView(View):  # нет возможности оттестировать на ошибки
    def get(self, request):
        template_name = "notebook/version.html"
        context = {
            "server_version": SERVER_VERSION
        }
        return render(
            request,
            template_name=template_name,
            context=context)


# Дополнительно вывести User по заданию

class AboutTemplateView(TemplateView):  # есть возможность оттестировать на ошибки
    template_name = "notebook/version.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["server_version"] = SERVER_VERSION
        return context

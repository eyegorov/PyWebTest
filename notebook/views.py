from django.shortcuts import render
from django.views import View

SERVER_VERSION = "0.0.1"


class IndexView(View):
    def get(self, request):
        return render(request, "notebook/index.html")


class AboutView(View):
    def get(self, request):
        context = {"server_version": SERVER_VERSION

                   }
        return render(request, "notebook/version.html", context=context)

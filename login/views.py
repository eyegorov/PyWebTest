from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


class LoginIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "login/index.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        return JsonResponse(request.POST, json_dumps_params={'indent': 4})

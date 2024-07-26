from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .models import *
from .forms import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.translation import gettext
from django.utils import translation
from django.conf import settings


class Home(ListView):
    template_name = "index.html"
    model = Details
    context_object_name = "data"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["form"] = DetailForms()
        return context

    def post(self, request):
        response_data = {}
        form = DetailForms(request.POST)
        if form.is_valid():
            response_data["name"] = form.cleaned_data["name"]
            response_data["age"] = form.cleaned_data["age"]
            response_data["phone"] = form.cleaned_data["phone"]
            form.save()
            print("hfhkashdkjashf")
            print(request.POST)
            return JsonResponse({"msg": "msg"})
        else:
            print("kldfkldshfkl")
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


from django.http import JsonResponse
from django.shortcuts import render
from .forms import DetailForms
from .models import Details

def home(request):
    form = DetailForms()
    if request.method == "POST":
        form = DetailForms(request.POST)
        if form.is_valid():
            detail = form.save()
            return JsonResponse({
                "name": detail.name,
                "age": detail.age,
                "phone": detail.phone
            })
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    return render(
        request,
        "index.html",
        {"form": form, "data": Details.objects.all()},
    )

def text(request):
    user_language = "es"
    translation.activate(user_language)
    response = HttpResponse(...)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response

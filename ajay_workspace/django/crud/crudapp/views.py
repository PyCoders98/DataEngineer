from typing import Any

# from django.db.models.query import _BaseQuerySet, QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from .models import *


class AboutPageView(DetailView):
    template_name = "about.html"
    model = Dummy
    context_object_name = "object_list"


class AboutPageView(ListView):
    template_name = "about.html"
    context_object_name = "object_list"
    model = Dummy
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["object_list"] = Dummy.objects.all()
    #     context["msg"] = "welcome to our site."
    #     return context


class ListPageView(ListView):
    model = Dummy
    template_name = "about2.html"
    paginate_by = 10
    # we can also rename context key default is object_list
    # context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["msg"] = "welcome to our site."
        return context

    def get_queryset(self):
        return self.model.objects.all()

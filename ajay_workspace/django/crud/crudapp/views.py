from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse

def home(request):
    officeform = OfficeForm()
    employeeform = EmployeeForm()
    context = {
        "officeform": officeform,
        "employeeform": employeeform,
    }
    return render(request, "index.html", context)


def office_crud(request):
    print(request.POST)
    return JsonResponse({"msg":"handle"})


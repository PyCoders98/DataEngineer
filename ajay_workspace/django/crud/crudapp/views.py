from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.forms import model_to_dict
from django.core import serializers


def home(request):
    officeform = OfficeForm()
    employeeform = EmployeeForm()
    context = {
        "officeform": officeform,
        "employeeform": employeeform,
    }
    return render(request, "index.html", context)


def office_crud(request):
    # print(request.POST)
    if request.method == "POST":
        print(request.POST)
    officeform = OfficeForm(request.POST)
    office = officeform.save()

    return JsonResponse(model_to_dict(office), safe=False)


def employee_crud(request):
    if request.method == "POST":
        id = request.POST.get("office")
        name = Office.objects.get(id=id)

        employeeform = EmployeeForm(request.POST)
        employee = employeeform.save()
        print(employee.office)
        return JsonResponse(model_to_dict(employee), safe=False)


def get_all_offices(request):
    offices = Office.objects.all()
    data = serializers.serialize("json", offices)
    return JsonResponse(data, safe=False)


def get_all_employees(request):
    employees = Employee.objects.all()
    data = serializers.serialize("json", employees)
    return JsonResponse(data, safe=False)

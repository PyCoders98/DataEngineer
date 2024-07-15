from django.shortcuts import render
from .forms import InputForm
from .models import *


def input_form_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # For now, you can just print the data to the console or save it to the database
            FormModel.objects.create(name=name, email=email, message=message)
            print(f"Name: {name}, Email: {email}, Message: {message}")
            # Redirect or render a success template
            return render(request, "success.html")
    else:
        form = InputForm()
    return render(request, "index.html", {"form": form})

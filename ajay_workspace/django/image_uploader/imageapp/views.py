from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout


# Create your views here.
def home(request):
    data = ImageModel.objects.all()
    context = {"data": data}
    return render(request, "user/index.html", context)


def image_portfolio(request, id):
    data = ImageModel.objects.get(id=id)
    print("calling")
    # print(data[0])
    print(request.POST.get("like"))
    if request.method == "POST":
        if request.POST.get("like") == "like":
            data.like += 1
        elif request.POST.get("like") == "dislike":
            data.dislike += 1
        else:
            return redirect(f"/comment-page/{id}")
        data.save()
        return redirect("/")


def get_image(request, id):
    data = ImageModel.objects.get(id=id)
    context = {"data": data}
    return render(request, "user/get_image.html", context)


def comment_page(request, id):
    data = ImageModel.objects.get(id=id)
    context = {"data": data}
    if request.method == "POST":
        data.comment = request.POST.get("comment")
        data.save()
        return redirect("/")
    return render(request, "user/comment_page.html", context)


def upload_image(request):
    if request.method == "POST":
        file = request.FILES.get("image")
        desc = request.POST.get("description")
        ImageModel.objects.create(image=file, desc=desc)
        messages.success(request, "Added Successfully.")
    return render(request, "admin/upload.html")


def confirmation_page(request, id):
    data = ImageModel.objects.get(id=id)
    return render(request, "admin/delete_confirmation_page.html", {"data": data})


def delete_image(request, id):
    data = ImageModel.objects.filter(id=id)
    data.delete()
    messages.info(request, "Deleted Successfully.")
    return redirect("/all-images/")


def edit_image(request, id):
    data = ImageModel.objects.get(id=id)
    if request.method == "POST":
        data.image = request.FILES.get("image")
        data.desc = request.POST.get("description")
        data.save()
        messages.success(request, "Image updated successfully.")
        return redirect("/all-images/")
    else:
        return render(request, "admin/edit_image.html", {"data": data})


def get_all_images(request):
    data = ImageModel.objects.all()
    context = {"data": data}
    return render(request, "admin/all_images.html", context)


# signup/login


def sign_up(request):
    if request.method == "POST":
        data = request.POST
        user = User.objects.filter(
            username=data["name"], email=data["email"], password=data["password"]
        )
        if user.exists():
            print("1")
            messages.info(request, 'User already exists')
            return redirect("/signup/")
        user = User.objects.create(
                username=data['name'],
                password=data['password'],
                email=data['email'],
            )
        
        messages.success(request, "User created successfully.")
        return redirect("/login/")
    return render(request,"login_signup/signup.html")


def login(request):
    if request.method == "POST":
        data = request.POST
        # query_set = User.objects.get()
        if not User.objects.filter(username=data['name']).exists():
            messages.info(request, "Invalid username or Password!")
            return redirect("/login/")
        else:

            user = authenticate(username=data['name'], password=data['password'])
        if user is None:

            messages.error(request,"Invalid Password!")
            return redirect("/login/")
        else:
            login(request)
            return redirect("/all-images/")
        # if data['email'] in 
    return render(request,"login_signup/login.html")
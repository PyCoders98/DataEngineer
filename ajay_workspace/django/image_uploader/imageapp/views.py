from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    data = ImageModel.objects.all()
    context = {"data": data}
    return render(request, "user/index.html", context)


@login_required(login_url="/login/")
def image_portfolio(request, id):
    data = ImageModel.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("like") == "like" or request.POST.get("like") == "dislike":
            like_data, created = ImageLike.objects.get_or_create(
                image=data, username=request.user.username
            )
            if request.POST.get("like") == "like":
                if like_data.like:
                    like_data.like = False
                    if data.like > 0:
                        data.like -= 1
                else:
                    like_data.like = True
                    data.like += 1
                    if like_data.dislike:
                        like_data.dislike = False
                        if data.dislike > 0:
                            data.dislike -= 1
            elif request.POST.get("like") == "dislike":
                if like_data.dislike:
                    like_data.dislike = False
                    if data.dislike > 0:
                        data.dislike -= 1
                else:
                    like_data.dislike = True
                    data.dislike += 1
                    if like_data.like:
                        like_data.like = False
                        if data.like > 0:
                            data.like -= 1

            like_data.save()
        else:
            return redirect(f"/comment-page/{id}")

        data.save()
        referring_url = request.META["HTTP_REFERER"]
        return redirect(referring_url)


def get_image(request, id):
    data = ImageModel.objects.get(id=id)
    context = {"data": data}
    return render(request, "user/get_image.html", context)


def comment_page(request, id):
    data = ImageModel.objects.get(id=id)
    comment_data = ImageComment.objects.filter(image=id)
    context = {"data": data, "comment": comment_data}
    if request.method == "POST":
        if request.user.is_authenticated:
            comment = request.POST.get("comment")
            print(request.user.username)
            ImageComment.objects.create(
                username=request.user.username, image=data, comment=comment
            )
            data.comment += 1
            data.save()
            return redirect("/")
        else:
            messages.info(request, "For comment you need to register first.")
            return render(request, "user/comment_page.html", context)
    return render(request, "admin/comment_page.html", context)


def profile(request):
    data = ImageModel.objects.filter(user=request.user)
    comment = ImageComment.objects.filter(image=request.user.id)
    context = {"data": data, "comment": comment}
    return render(request, "admin/profile.html", context)


def update_profile_picture(request, id):
    # data = ImageModel.objects.get(id=id)
    # if request.method == "POST":
    #     image = request.FILES("image")
    #     data.image = image
    #     data.save()
    #     messages.info(request, "Profile Updated Successfully!")
    #     return redirect("/profile/")
    return render(request, "admin/update_profile_picture.html")


@login_required(login_url="/login/")
def upload_image(request):
    if request.method == "POST":
        file = request.FILES.get("image")
        desc = request.POST.get("description")
        data = ImageModel.objects.create(user=request.user, image=file, desc=desc)
        ImageLike.objects.create(username=request.user.username, image=data)
        messages.success(request, "Added Successfully.")
    return render(request, "admin/upload.html")


@login_required(login_url="/login/")
def confirmation_page(request, id):

    data = ImageModel.objects.get(id=id)
    return render(request, "admin/delete_confirmation_page.html", {"data": data})


@login_required(login_url="/login/")
def delete_image(request, id):
    data = ImageModel.objects.filter(id=id)
    data.delete()
    messages.info(request, "Deleted Successfully.")
    return redirect("/profile/")


@login_required(login_url="/login/")
def edit_image(request, id):
    data = ImageModel.objects.get(id=id)
    if request.method == "POST":
        data.image = request.FILES.get("image")
        data.desc = request.POST.get("description")
        data.save()
        messages.success(request, "Image updated successfully.")
        return redirect("/profile/")
    else:
        return render(request, "admin/edit_image.html", {"data": data})


@login_required(login_url="/login/")
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
            messages.info(request, "User already exists")
            return redirect("/signup/")
        else:
            if data["password"] == data["confirm_password"]:
                user = User.objects.create(
                    username=data["name"],
                    password=data["password"],
                    email=data["email"],
                )
                user.set_password(data["password"])
                user.save()
                messages.success(
                    request, "User created successfully.You can login now."
                )
                return redirect("/login/")
            else:
                messages.info(request, "Password does not match")
    return render(request, "login_signup/signup.html")


def login_fun(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username or Password!")
            return redirect("/login/")

        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.error(request, "Invalid Password!")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")

    return render(request, "login_signup/login.html")


def logout_confirm(request):
    return render(request, "admin/logout_confirmation_page.html")


def logout_fun(request):
    logout(request)
    return redirect("/")

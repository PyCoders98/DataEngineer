from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import *
from django.templatetags.static import static
from django.views.generic import ListView
from django.conf import settings
import json
from django.http import JsonResponse
from django.forms import model_to_dict
from django.core import serializers
from django.core.mail import send_mail


# ----------------Explore Page----------------
class Explore(ListView):
    model = ImageModel
    context_object_name = "data"
    template_name = "user/index.html"
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


# ----------------Home Page----------------
class Home(View):
    def get(self, request):
        follower = FollowerModel.objects.filter(follower=request.user).values('user')
        queryset = ImageModel.objects.filter(user__in=follower)
        context = {"data": queryset}
        return render(request, "admin/home_page.html", context)


# ----------------following Posts----------------
def h(request):
    pass


# ----------------Follow button----------------
def follow(request, id):
    pass


# ----------------follow saving requests----------------
@login_required(login_url="/login/")
def follow_request(request, id):
    current_user = request.user
    post = ImageModel.objects.get(id=id)
    post_admin = post.user
    response_data = {}

    if request.method == "POST":
        try:
            data = RequestModel.objects.get(
                receiver_user=post_admin, sender_user=request.user
            )
            data.delete()
            response_data["total_requests"] = RequestModel.objects.filter(
                receiver_user=post_admin, sender_user=request.user
            ).count()
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )
        except:
            data = RequestModel.objects.create(
                receiver_user=post_admin, sender_user=request.user
            )
            response_data["total_requests"] = RequestModel.objects.filter(
                receiver_user=post_admin, sender_user=request.user
            ).count()
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )
    else:
        response_data["total_requests"] = RequestModel.objects.filter(
            receiver_user=post_admin, sender_user=request.user
        ).count()
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def all_requests(request):
    current_user = request.user
    requests = RequestModel.objects.filter(receiver_user=current_user)
    return render(request, "admin/requests.html", {"requests": requests})


# ----------------Accept or Cencel follow requests----------------
def accept_request(request, id):
    current_user = request.user
    requested_user = User.objects.get(id=id)

    requests = RequestModel.objects.filter(receiver_user=current_user)
    if request.method == "POST":
        if request.POST.get("accept") == "accept":
            FollowerModel.objects.create(user=current_user, follower=requested_user)
            RequestModel.objects.filter(
                receiver_user=current_user, sender_user=requested_user
            ).delete()
        else:
            RequestModel.objects.filter(
                receiver_user=current_user, sender_user=requested_user
            ).delete()
        return redirect("/all-requests")

    return redirect("/all-requests/")


# ----------------Image portfolio (like, dislike, comment functionality)----------------
@login_required(login_url="/login/")
def image_portfolio(request, id):
    data = ImageModel.objects.get(id=id)
    if request.method == "POST":

        response_data = {}
        if request.POST.get("like") == "like":
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

            like_data.save()
            data.save()
            response_data["like"] = data.like
            response_data["dislike"] = data.dislike
            response_data["status"] = "success"
            return HttpResponse(
                json.dumps(response_data), content_type="application/json"
            )
        else:
            return redirect(f"/comment-page/{id}")


def get_like_dislike_count(request, id):
    image = ImageModel.objects.get(id=id)
    response = {}
    response["like"] = image.like
    response["dislike"] = image.dislike

    return JsonResponse(response, safe=False)


# ----------------Open image to download----------------
def get_image(request, id):
    data = ImageModel.objects.get(id=id)
    context = {"data": data}
    return render(request, "user/get_image.html", context)


# ----------------Comment on any image----------------
def comment_page(request, id):
    data = ImageModel.objects.get(id=id)
    comment_data = ImageComment.objects.filter(image=id)
    context = {"data": data, "comments": comment_data}
    if request.method == "POST":
        if request.user.is_authenticated:
            comment = request.POST.get("comment")
            ImageComment.objects.create(user=request.user, image=data, comment=comment)
            data.comment += 1
            data.save()
            return redirect("/")
        else:
            messages.info(request, "For comment you need to register first.")
            return render(request, "user/comment_page.html", context)
    return render(request, "admin/comment_page.html", context)


# ----------------User personnel profile----------------
def profile(request):
    data = ImageModel.objects.filter(user=request.user)
    comment = ImageComment.objects.filter(image=request.user.id)
    context = {"data": data, "comment": comment}
    return render(request, "admin/profile.html", context)


# ----------------View profile image----------------
def view_profile_image(request, id):
    return render(request, "admin/view_profile_image.html")


# ----------------Update profile image----------------
class UpdateProfileImageView(View):
    template = "admin/update_profile_image.html"

    def get(self, request):
        form = ProfileImage()
        return render(request, self.template, {"form": form})

    def post(self, request):
        user_profile = User.objects.get(id=request.user.id)
        form = ProfileImage(request.POST, request.FILES)
        if form.is_valid():
            user_profile.profile_image = request.FILES.get("profile_image")
            user_profile.save()
            messages.success(request, "Updated successfully!")
            return redirect(f"/view-profile-image/{request.user.id}")


# ----------------Remove profile image----------------
class DeleteProfileImageView(View):
    template = "admin/remove_profile_image_confirmation.html"

    def get(self, request):
        profile = User.objects.get(id=request.user.id)
        return render(request, self.template)

    def post(self, request):
        user_profile = User.objects.get(id=request.user.id)
        user_profile.profile_image = None
        user_profile.save()
        messages.success(request, "Image removed successfully!")
        return redirect(f"/view-profile-image/{request.user.id}")


# ----------------Upload image----------------
@login_required(login_url="/login/")
def upload_image(request):
    if request.method == "POST":
        file = request.FILES.get("image")
        desc = request.POST.get("description")
        data = ImageModel.objects.create(user=request.user, image=file, desc=desc)
        ImageLike.objects.create(username=request.user.username, image=data)
        messages.success(request, "Added Successfully.")
    return render(request, "admin/upload.html")


# ----------------Confirmateion : Delete uploaded image from site ----------------
@login_required(login_url="/login/")
def confirmation_page(request, id):
    data = ImageModel.objects.get(id=id)
    return render(request, "admin/delete_confirmation_page.html", {"data": data})


# ----------------Delete uploaded image from site----------------
@login_required(login_url="/login/")
def delete_image(request, id):
    data = ImageModel.objects.filter(id=id)
    data.delete()
    messages.info(request, "Deleted Successfully.")
    return redirect("/profile/")


# ----------------Update uploaded image from site----------------
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


# ----------------User login/signup functionality----------------
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
                subject = "Welcome to the ImageSphere!"
                message = f"{user.username}, thank you for beign a part of ImageSphere."
                email_from = settings.EMAIL_HOST_USER
                receipient_list = [
                    user.email,
                ]
                send_mail(subject, message, email_from, receipient_list)
                return redirect("/login/")
            else:
                messages.info(request, "Password does not match")
    return render(request, "login_signup/signup.html")


def login_fun(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        data = User.objects.filter(username=username).values_list("email", flat=True)
        if not data.exists():
            messages.error(request, "Invalid username or Password!")
            return redirect("/login/")
        user = authenticate(username=username, password=password)
        if user is None:

            messages.error(request, "Invalid Password!")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/")
    return render(request, "login_signup/login.html")


# ----------------Logout confirmation page----------------
def logout_confirm(request):
    return render(request, "admin/logout_confirmation_page.html")


def logout_fun(request):
    logout(request)
    return redirect("/")

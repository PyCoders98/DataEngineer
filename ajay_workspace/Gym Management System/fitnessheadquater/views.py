from django.shortcuts import render, redirect

from fitnessheadquater.models import *
from django.contrib import messages
import math
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime
import time
from django.urls import reverse
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from rest_framework.response import Response
from django.http import JsonResponse


key = "rzp_test_zoEqBo2vt3lNJ5"
secret_key = "CJg2C3rtKfkfo4aBInIYc9h3"


def check_member(request):
    try:
        query_set = Member.objects.get(user__user=request.user)
        member = True
    except:
        member = False
    return member


def check_staff(request):
    if request.user.is_staff:
        staff = True
    else:
        staff = False
    return staff


def home(request):
    member = check_member(request)
    staff = check_staff(request)
    context = {"member": member, "staff": staff}
    return render(request, "user/index.html", context)


def user_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        if not User.objects.filter(username=name).exists():
            messages.error(request, "Invalid username or password")
            return redirect("/login/")
        password = request.POST.get("password")
        user_auth = authenticate(username=name, password=password)

        if user_auth is None:
            messages.error(request, "Invalid password")
            return redirect("/login/")
        else:
            login(request, user_auth)
            if request.user.is_staff:
                return redirect("/admin-home/memberships/")
            return redirect("/membership/")
    return render(request, "login/login.html")


def signup(request):
    if request.method == "POST":
        data = request.POST
        username = data["name"]
        password = data["password"]
        email = data["email"]
        normalize_email = email.lower()
        confirm_password = data["confirm_password"]
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User already exists")
            return redirect("/signup/")
        if confirm_password == password:
            user = User.objects.create(
                username=username, email=normalize_email, password=password
            )
            user.set_password(password)
            user.save()
            contact = data["contact"]
            age = data["age"]
            address = data["address"]
            gender = data["gender"]

            user_info = SiteMember.objects.create(
                user=user,
                contact=contact,
                age=age,
                address=address,
                gender=gender,
            )
            user_info.save()
            messages.info(request, "Account created Successfully")
            return redirect("/signup/")
        else:
            messages.info(request, "Password  does not match")
    return render(request, "login/signup.html")


def logout_page(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login/")
def buy_pack(request, id):
    user = SiteMember.objects.get(user=request.user)
    if Member.objects.filter(user=user).exists():
        messages.info(request, "You already bought a pack.")
        referring_url = request.META.get("HTTP_REFERER")
        return redirect(referring_url)
    else:
        return redirect(reverse("buy_pack_confirm", args=[id]))


@csrf_exempt
def buy_pack_confirm(request, id):

    pack_data = Packs.objects.get(id=id)
    user = SiteMember.objects.get(user=request.user)

    price = int(pack_data.price) * 100  # Convert price to paise
    name = request.user.username  # Use request.user directly
    if Member.objects.filter(user=user).exists():
        messages.info(request, "You already bought a pack.")
        return redirect(reverse("personnel_info", args=[id]))
    else:
        client = razorpay.Client(auth=(key, secret_key))  # Replace with actual keys
        # Construct the redirect URL using reverse() function

        payment = client.order.create(
            {
                "amount": price,
                "currency": "INR",
                "payment_capture": "1",
            }
        )
        duration = pack_data.duration
        end_date = datetime.now() + timedelta(days=int(duration * 30))

        member = Member.objects.create(
            user=user,
            pack_duraton=pack_data.duration,
            pack_title=pack_data.title,
            pack_price=pack_data.price,
            member=True,
            end_date=end_date,
        )
        context = {
            "pack_data": pack_data,
            "payment": payment,
        }

        return render(request, "user/buy_confirm.html", context)


@csrf_exempt
def greeting_page(request):
    subject = "Fitness Headquater"
    html_content = render_to_string(
        "mail_template/greeting_mail.html",
        {"receipient_name": request.user.username},
    )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        request.user.email,
    ]
    email = EmailMultiAlternatives(subject, "", email_from, recipient_list)
    email.attach_alternative(html_content, "text/html")
    email.send()
    return render(request, "user/greeting_page.html")


def offer(request):
    member = check_member(request)
    query_set = Packs.objects.filter(category__category="Offer")
    if query_set.count() == 0:
        query_set = None
    context = {"offer": query_set, "member": member, "staff": check_staff(request)}
    return render(
        request,
        "user/offer.html",
        context,
    )


def membership(request):
    member = check_member(request)
    query_set = Packs.objects.filter(category__category="Membership")
    return render(
        request,
        "user/membership.html",
        {"membership": query_set, "member": member, "staff": check_staff(request)},
    )


def career(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        normalized_email = email.lower()
        contact = request.POST.get("contact")
        age = request.POST.get("age")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        cv = request.FILES["cv"]
        print(normalized_email)
        Applicant.objects.create(
            name=name,
            email=normalized_email,
            contact=contact,
            age=age,
            address=address,
            gender=gender,
            file=cv,
        )
        messages.success(request, "Success! Your Request was sent successfully.")
    member = check_member(request)
    return render(
        request, "user/career.html", {"member": member, "staff": check_staff(request)}
    )


def about(request):
    member = check_member(request)
    return render(
        request, "user/aboutus.html", {"member": member, "staff": check_staff(request)}
    )


def contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        normalize_email = email.lower()
        text = request.POST.get("text")
        ContactUs.objects.create(
            name=name,
            email=normalize_email,
            comment=text,
        )
        messages.success(request, "Submitted Successfully")
    member = check_member(request)
    return render(
        request,
        "user/contactus.html",
        {"member": member, "staff": check_staff(request)},
    )


def personnel_info(request, id):
    query_set = Member.objects.get(user__user=request.user.id)
    buy_date = query_set.buy_date.date()
    end_date = query_set.end_date.date()
    member = check_member(request)
    context = {
        "info": query_set,
        "end_date": end_date,
        "buy_date": buy_date,
        "member": member,
    }
    return render(request, "user/personnel_info.html", context)


def update_personnel_info(request, id):
    query_set = Member.objects.get(user__user=id)
    gender = query_set.user.gender.lower()
    member = check_member(request)
    context = {"info": query_set, "current_gender": gender, "member": member}
    if request.method == "POST":
        current_user = SiteMember.objects.get(user=query_set.user.user.id)
        print(current_user)
        gender = request.POST.get("gender")
        contact = request.POST.get("contact")
        address = request.POST.get("address")
        age = request.POST.get("age")
        current_user.age = age
        current_user.gender = gender
        current_user.contact = contact
        current_user.address = address
        current_user.save()
        messages.success(request, "Updated Successfully")
        return redirect(reverse("personnel_info", args=[id]), context)
    return render(request, "user/update_personnel_info.html", context)


def admin_home(request):
    staff = check_staff(request)
    context = {"staff": staff}
    return render(request, "admin/home_page.html", context)


def admin_memberships(request):
    response_data = {}
    if request.method == "POST":
        category = Categori.objects.get(category="Membership")
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        price = request.POST.get("price")
        regular_price = request.POST.get("regular_price")
        discount = int(((int(regular_price) - int(price)) * 100) / int(regular_price))
        Packs.objects.create(
            category=category,
            title=name,
            duration=duration,
            price=price,
            regular_price=regular_price,
            discount=discount,
        )

        # messages.success(request, "Added Successfully")
        print(response_data)
        return JsonResponse(
            list(Packs.objects.filter(category__category="Membership").values()),
            safe=False,
        )
    query_set = Packs.objects.filter(category__category="Membership")
    return render(request, "admin/admin_memberships.html", {"membership": query_set})


def update_memberships(request, id):

    data = Packs.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        price = request.POST.get("price")
        regular_price = request.POST.get("regular_price")

        data.title = name
        data.duration = duration
        data.price = price
        data.regular_price = regular_price
        data.discount = int(
            ((int(regular_price) - int(price)) * 100) / int(regular_price)
        )
        data.save()
        return redirect("/admin-home/memberships/")
    return render(request, "admin/update_membership.html", {"data": data})


def delete_memberships(request, id):
    data = Packs.objects.get(id=id)
    data.delete()
    return JsonResponse(
        list(Packs.objects.filter(category__category="Membership").values()),
        safe=False,
    )


def admin_offers(request):
    reminder = True
    if request.method == "POST":
        category = Categori.objects.get(category="Offer")
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        price = request.POST.get("price")
        regular_price = request.POST.get("regular_price")
        discount = int(((int(regular_price) - int(price)) * 100) / int(regular_price))
        Packs.objects.create(
            category=category,
            title=name,
            duration=duration,
            price=price,
            regular_price=regular_price,
            discount=discount,
        )
        messages.success(request, "Added Successfully")
    query_set = Packs.objects.filter(category__category="Offer")
    if not query_set.exists():
        reminder = False

    return render(
        request, "admin/admin_offers.html", {"offer": query_set, "reminder": reminder}
    )


def update_offers(request, id):
    data = Packs.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        price = request.POST.get("price")
        regular_price = request.POST.get("regular_price")
        data.title = name
        data.duration = duration
        data.price = price
        data.regular_price = regular_price
        data.discount = int(
            ((int(regular_price) - int(price)) * 100) / int(regular_price)
        )
        data.save()
        return redirect("/admin-home/offers/")
    return render(request, "admin/update_offer.html", {"data": data})


def delete_offers(request, id):
    data = Packs.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        return redirect("/admin-home/offers/")
    return render(request, "admin/delete_offer.html")


def members(request):
    query_set = Member.objects.all()
    context = {"members": query_set}
    return render(request, "admin/members_page.html", context)


def admin_career(request):
    if request.GET.get("search"):
        search_key = request.GET.get("search")
        query_set = Applicant.objects.filter(
            Q(name__icontains=search_key)
            | Q(email__icontains=search_key)
            | Q(contact__icontains=search_key)
            | Q(address__icontains=search_key)
            | Q(gender__exact=search_key)
        ).order_by("-apply_date")
    else:
        query_set = Applicant.objects.all().order_by("-apply_date")
    total_applicants = query_set.count()
    paginator = Paginator(query_set, 15)
    page_number = request.GET.get("page", 1)
    query_set = paginator.get_page(page_number)
    return render(
        request,
        "admin/career_page.html",
        {
            "applicant": query_set,
            "page_number": page_number,
            "total_records": total_applicants,
        },
    )


def admin_contactus(request):
    query_set = ContactUs.objects.all()
    total_records = ContactUs.objects.all().count()

    paginator = Paginator(query_set, 15)
    page_number = request.GET.get("page", 1)
    query_set = paginator.get_page(page_number)

    return render(
        request,
        "admin/admin_contactus.html",
        {
            "queryset": query_set,
            "page_number": page_number,
            "total_records": total_records,
        },
    )

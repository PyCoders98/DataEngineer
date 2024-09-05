from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models  import Q
# import urllib.parse
# Create your views here.


# @login_required(login_url="/login-page/")
def index(request):
    if request.GET.get("filter") != None:
        filter = request.GET["filter"]
    else:
        filter="All"
    search_key=""
    data = Receipe.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page', 1)
    data = paginator.get_page(page_number)

    if request.GET.get("search"):
        search_key = request.GET.get("search")
        data = Receipe.objects.filter(
            Q(receipe_name__icontains=search_key) | 
            Q(category__category__icontains = search_key)
            )
        filter="All"
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page', 1)
        data = paginator.get_page(page_number)
    if request.GET.get("filter") != None and request.GET.get("filter") != "All":
        filter = request.GET.get("filter")
        data = Receipe.objects.filter(category__category=request.GET.get("filter"))
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page', 1)
        data = paginator.get_page(page_number)
    elif request.GET.get("filter") != None and request.GET.get("filter") != "All" and request.GET.get("search")==None:
        filter = request.GET.get("filter")
        data = Receipe.objects.filter(category__category=request.GET.get("filter"))
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page', 1)
        data = paginator.get_page(page_number)
    
    return render(request, 'index.html', {"data":data,"filter":filter,"search":search_key, "page_number":page_number})




def view_receipe(request, id):
    data = Receipe.objects.get(id=id)
    return render(request, 'view_receipe.html', {"data":data})
    

def receipes(request):
    if not request.user.is_authenticated:
        return redirect("/login-page/")
    if request.method == "POST":
        data = request.POST
        category_obj = Category.objects.get(category=data['category'])
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_ingredients = data.get("receipe_ingredients")
        receipe_making_process = data.get("making_process")
        Receipe.objects.create(receipe_image=receipe_image, receipe_name=receipe_name, receipe_description=receipe_description, category=category_obj, user=request.user, receipe_ingredients=receipe_ingredients, receipe_making_process=receipe_making_process)
        return redirect("/receipes/")
    queryset = Receipe.objects.all()
    context = {"receipe":queryset}
    return render(request, "receipes.html", context)


@login_required(login_url="/login-page/")
def show_all(request):
    
    data = Receipe.objects.all().filter(user=request.user)
    if request.GET.get('search'):
        search_key = request.GET.get('search')
        data = data.filter(receipe_name__icontains=search_key)
    if request.GET.get("filter") != None and request.GET.get("filter") != "All":
        data = data.filter(category__category=request.GET.get("filter"))

    print
    return render(request, "show_all.html", {"data":data, "filter":request.GET.get("filter")})


def delete_receipe(request, id):
    if not request.user.is_authenticated:
        return redirect("/login-page/")

    if request.method=='POST':
        queryset = Receipe.objects.get(id=id)
        print(queryset.receipe_name)
        # queryset.delete()
        return redirect("/all-receipes/")
    return render(request,"delete_receipe.html")


def update_receipe(request, id):
    if not request.user.is_authenticated:
        return redirect("/login-page/")
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        category = Category.objects.get(category=request.POST["category"])
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        receipe_ingredients = request.POST.get("receipe_ingredients")
        print(receipe_ingredients)
        receipe_making_process = request.POST.get("receipe_making_process")
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        queryset.receipe_ingredients = receipe_ingredients
        queryset.receipe_making_process = receipe_making_process

        queryset.category = category
        
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("/all-receipes/")
       
    return render(request, "update_receipe.html", {"receipe":queryset})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid username or Password")
            return redirect("/login-page/")
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login-page/")
        
        else:
            login(request, user)
            return redirect("/receipes/")

    return render(request, "login.html")  


def logout_page(request):
    logout(request)
    return  redirect("/") 


def register_page(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        user = User.objects.filter(username=user_name)

        if user.exists():
            messages.info(request, 'User already exists')
            return redirect("/register-page/")
        if password == confirm_password:
            user = User.objects.create(
                username=user_name,
                password=password,
                email=email,
            )
            user.set_password(password)
            user.save()
            messages.info(request, "Account created Successfully")
            return redirect("/register-page/")
        else:
            messages.info(request, "Password  does not match")

    return render(request, "register.html")


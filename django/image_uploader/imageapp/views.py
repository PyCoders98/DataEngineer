from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    data = ImageModel.objects.all()
    context = {"data": data}
    return render(request, "user/index.html", context)


def upload_image(request):
    if request.method == "POST":
        file = request.FILES.get("image")
        desc = request.POST.get("description")
        ImageModel.objects.create(image=file, desc=desc)
        messages.success(request, "Added Successfully.")
    return render(request, "admin/upload.html")


def confirmation_page(request,id):
    data = ImageModel.objects.get(id=id)
    return render(request, "admin/delete_confirmation_page.html", {"data":data})

def delete_image(request, id):
    data = ImageModel.objects.filter(id=id)
    data.delete()
    messages.success(request, "Deleted Successfully.")
    return redirect("/all-images/")
    
def edit_image(request,id):
    data = ImageModel.objects.get(id = id)
    if request.method == "POST":
        data.image = request.FILES.get('image')
        data.desc = request.POST.get('description')
        data.save()
        messages.success(request,"Image updated successfully.")
        return redirect("/all-images/")
    else:
        return render(request,'admin/edit_image.html',{"data":data})
        
def get_all_images(request):
    data = ImageModel.objects.all()
    context = {"data": data}
    return render(request, "admin/all_images.html", context)

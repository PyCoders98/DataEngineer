from .models import *


def profile_image(request):
    profile = ImageModel.objects.filter(user__id=request.user.id).first()
    return {"profile": profile}


def follow_count(request):
    if request.user.is_authenticated:
        request_count = RequestModel.objects.filter(receiver_user=request.user).count()
        print(request_count)
        return{"request_count":request_count}
    else:
        return {"request_count":0}
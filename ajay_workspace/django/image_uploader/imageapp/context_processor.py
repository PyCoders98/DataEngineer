from .models import *


def profile_image(request):
    profile = ImageModel.objects.filter(user__id=request.user.id).first()
    return {"profile": profile}


def follow_count(request):
    if request.user.is_authenticated:
        request_count = RequestModel.objects.filter(receiver_user=request.user).count()
        return {"request_count": request_count}
    else:
        return {"request_count": 0}


def followers_count(request):
    if request.user.is_authenticated:
        followers_count = FollowerModel.objects.filter(user=request.user)
        return {"followers_count": followers_count.count()}
    else:
        return {"followers_count": 0}
    
def following_count(request):
    if request.user.is_authenticated:
        following_count = FollowerModel.objects.filter(follower=request.user)
        return {"following_count": following_count.count()}
    else:
        return {"following_count": 0}


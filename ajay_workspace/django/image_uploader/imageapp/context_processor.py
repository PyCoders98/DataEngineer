from .models import *


def profile_image(request):
    profile = ImageModel.objects.filter(user__id=request.user.id).first()
    return {"profile": profile}

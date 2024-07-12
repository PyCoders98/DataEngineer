from .models import *


def profile_image(request):
    profile = ImageModel.objects.filter(user__id=request.user.id).first()
    print()
    # print(profile[0].pofile_image)
    return {"profile": profile}

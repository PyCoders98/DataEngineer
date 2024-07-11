from .models import *


def liked(request, id):
    liked = False
    image = ImageLike.objects.get(id=id)
    if request.user in image:
        liked = True
    return {liked}

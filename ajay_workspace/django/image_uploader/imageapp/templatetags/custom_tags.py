# myapp/templatetags/custom_tags.py

from django import template
from imageapp.models import *

register = template.Library()


@register.simple_tag(takes_context=True)
def is_liked(context, id):
    request = context["request"]
    lst = []
    liked = False
    try:
        data = ImageLike.objects.filter(image__id=id).values("username", "like")
        for i in data:
            lst.append(i)
        for i in lst:
            if i["username"] == request.user.username:
                if i["like"]:
                    liked = True
                    return liked
                else:
                    return liked
    except:
        return liked


@register.simple_tag(takes_context=True)
def is_disliked(context, id):
    request = context["request"]
    lst = []
    liked = False
    try:
        data = ImageLike.objects.filter(image__id=id).values("username", "dislike")
        for i in data:
            lst.append(i)
        for i in lst:
            if i["username"] == request.user.username:
                if i["dislike"]:
                    liked = True
                    return liked
                else:
                    return liked
    except:
        return liked


@register.simple_tag(takes_context=True)
def is_followed(context, id):
    request = context["request"]
    lst = []
    if request.user.is_authenticated:
        post_admin = FollowerModel.objects.filter(follower=request.user).values("user")

        for admin in post_admin:
            post_admin_id = admin['user']
            lst.append(post_admin_id)
        if id in lst:
            return True
        return False
    return False

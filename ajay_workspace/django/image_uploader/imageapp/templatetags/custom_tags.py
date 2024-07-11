# myapp/templatetags/custom_tags.py

from django import template
from imageapp.models import ImageLike

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
        print(lst)
        for i in lst:
            if i["username"] == request.user.username:
                if i["like"]:
                    liked = True
                    return liked
                else:
                    return liked
    except:
        return liked

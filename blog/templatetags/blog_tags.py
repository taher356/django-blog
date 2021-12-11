from django import template

register = template.Library()
from blog.models import PostModel


@register.simple_tag(name="totalposts")
def function():
    posts = PostModel.objects.filter(status=1).count() 
    return posts


@register.simple_tag(name="posts")
def function():
    posts = PostModel.objects.filter(status=1)
    return posts
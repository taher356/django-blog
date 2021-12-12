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

@register.filter()
def snippet(value):
    return value[:20] +  '...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def popularposts():
    posts = PostModel.objects.filter(status=1).order_by('publish_date')[:3] 
    return  {'posts': posts}  
from django.shortcuts import render
from blog.models import PostModel
# Create your views here.
def blog_view(request):
    Post = PostModel.objects.filter(status=1 )
    context = {'PostModel':Post}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request,pid):
    post = PostModel.objects.get(id=pid)
    context = {'post':post}
    return render(request,'test.html',context)    
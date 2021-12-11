from django.shortcuts import render,get_object_or_404
from blog.models import PostModel
# Create your views here.
def blog_view(request):
    posts = PostModel.objects.filter(status=1)
    context = {'PostModel':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = PostModel.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def test(request,):
   
    return render(request,'test.html')    
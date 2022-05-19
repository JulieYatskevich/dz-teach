from django.shortcuts import render
from .models import Post

def blog_home(request):
    post = Post.objects.all()
    return render(request, 'blog/blog_home.html', {'post': post})

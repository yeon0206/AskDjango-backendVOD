# blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    ctx={
        'post_list': qs,
    }
    return render(request, 'blog/post_list.html',ctx)
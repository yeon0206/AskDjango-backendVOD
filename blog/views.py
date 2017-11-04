# blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','') #request get 쿼리셋어 q가있으면 가져오고, 없으면 빈문자열
    if q:
        qs = qs.filter(title__icontains=q)

    ctx={
        'post_list': qs,
        'q' : q,
    }
    return render(request, 'blog/post_list.html',ctx)
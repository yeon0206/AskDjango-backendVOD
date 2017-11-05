# blog/views.py
from django.http import Http404
from django.shortcuts import get_object_or_404, render
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

'''
파이썬 dict타입에서도 지원하는 인터페이스입니다. request.GET은 QuerySet타입으로서, dict과 유사한 인터페이스를 제공해주고 있습니다.
QuerySet의 get함수는 인자를 1개 받기도 하고, 2개 받을 수도 있습니다.

>>> queryset[접근Key] # 지정 Key의 값 반환을 시도. 지정 Key가 없을 때 KeyError 예외가 발생합니다.

>>> queryset.get(접근Key) # 지정 Key의 값 반환을 시도. 지정 Key가 없을 때 KeyError 예외가 발생합니다.

>>> queryset.get(접근Key, 디폴트값) # queryset에 지정Key가 없을 때, KeyError 예외가 발생하지 않고, 2번째 인자로 지정한 디폴트값이 리턴됩니다.
'''

def post_detail(request, id):
    #url창에 localhost:8000/blog/10 을 적어주면, id=10을 받는다
    #Post 게시물 하나를 지우고 다시 접근하면 서버에러 500을 발생시킴
    #서버에러가 아니기때문에 Http404에러를 발생시켜줘야한다.
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, id=id)

    ctx={
        'post':post,
    }
    return render(request, 'blog/post_detail.html', ctx)

# Post.objects.all() 은 QuerySet 이며,

# QuerySet 의 filter 와 exclude, order_by 리턴값은 QuerySet 입니다.
# QuerySet 의 get 리턴값은 해당 모델의 인스턴스이구요.
# 잘 안 넘어간다고 하신. 아래 코드에서도 QuerySet 인스턴스가 post 변수에 담겨집니다.

# post = Post.objects.all().filter(id=pk)
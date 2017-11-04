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

'''
파이썬 dict타입에서도 지원하는 인터페이스입니다. request.GET은 QuerySet타입으로서, dict과 유사한 인터페이스를 제공해주고 있습니다.
QuerySet의 get함수는 인자를 1개 받기도 하고, 2개 받을 수도 있습니다.

>>> queryset[접근Key] # 지정 Key의 값 반환을 시도. 지정 Key가 없을 때 KeyError 예외가 발생합니다.

>>> queryset.get(접근Key) # 지정 Key의 값 반환을 시도. 지정 Key가 없을 때 KeyError 예외가 발생합니다.

>>> queryset.get(접근Key, 디폴트값) # queryset에 지정Key가 없을 때, KeyError 예외가 발생하지 않고, 2번째 인자로 지정한 디폴트값이 리턴됩니다.
'''
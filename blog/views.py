# blog/views.py
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect,render
from .models import Post, Comment
from .forms import PostForm
from django.views.generic import ListView

def post_list(request):
    # print(request.user.is_authenticated)
    qs = Post.objects.all().prefetch_related('tag_set')
    #MtoM or FK의 reverse relation
    #Post에서 Commnet 접근, Tag접근
    q = request.GET.get('q','') #request get 쿼리셋어 q가있으면 가져오고, 없으면 빈문자열
    if q:
        qs = qs.filter(title__icontains=q)

    ctx={
        'post_list': qs,
        'q' : q,
    }
    return render(request, 'blog/post_list.html',ctx)

# post_list = ListView.as_view(model=Post, paginate_by=10)
    
    # HttpResponse 인스턴스인데, render를 통해서, 좀 더 쉽게 템플릿을 통한 렌더링
    # response=render(request, 'blog/post_list.html',ctx)
    # return response

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

def post_new(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post) #post.get_absolute_url() => post detail
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form':form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request,'포스팅을 수정했습니다.')
            return redirect(post) #post.get_absolute_url() => post detail
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form':form,
    })

def comment_list(request):
    comment_list = Comment.objects.all().select_related('post') 
    #Comment에 대한 sql을 요청할때 한번에 같이 Post sql을 요청한다.
    #외래키 or 원투원 필드를 쓸 때 활용. 생성되는 sql수를 현저하게 줄일 수 있다. 
    # SELECT ••• FROM "blog_comment" INNER JOIN "blog_post" ON ("blog_comment"."post_id" = "blog_post"."id")
    return render(request, 'blog/comment_list.html',{
        'comment_list' : comment_list,    
    })
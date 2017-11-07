# dojo/views.py
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post
'''
def mysum(request,x,y=0,z=0): #y=0,z=0으로 default 값을 지정해준다.
#view함수는 클라이언트가 서버로 넘길때, 첫번째 인자는 무조건 request를 받는다.
#request: HttpRequest 는 request의 인스턴스
    return HttpResponse(int(x)+int(y)+int(z))
'''

def post_new(request):
    if request.method == 'POST':
        #POST인자는 request.POST, request.FILES를 제공받음.
        form=PostForm(request.POST, request.FILES)
        
        #인자로 받은 값에 대해서, 유효성 검증 수행
        if form.is_valid(): #현재 폼에 모든validator 모든 에러가 발생하지 않는다면 True를 리턴
            #검증에 성공한 값들을 사전타입으로 제공받음.
            #검증에 성공한 값을 제공받으면 Django Form의 역할을 여기까지!
            #필요에 따라, 이 값을 DB에 저장하기
            
            # # 방법1)
            '''
            # print(form.cleaned_data) #사전형식으로 출력
            post = Post() #Post인스턴스생성
            post.title=form.cleaned_data['title']
            post.content=form.cleaned_data['content']
            post.save()
            '''
            #방법2)
            '''
            post = Post(title=form.cleaned_data['title'],
                        content=form.cleaned_data['content'])
            post.save()
            '''

            #방법3)
            ''''
            post = Post.objects.create(title=form.cleaned_data['title'],
                                     content=form.cleaned_data['content'])
            '''
            #방법4)
            post = Post.objects.create(**form.cleaned_data)

            return redirect('/dojo/') #namespace:name
        else: #검증에 실패하면, form.errors와 form.각필드.errors에 오류정보를 저장 
            form.errors
    else:
        form=PostForm() # 빈 폼
    ctx={
        'form':form,
    }
    return render(request, 'dojo/post_form.html',ctx)

def mysum(request,numbers):
    # numbers = "1/2/12/123/12312/312/123123"
    # result=sum(map(int, numbers.split('/')))  
    # /슬러쉬가 하나이상 들어가도 실행이 됨> 그런데 // 사이에 빈문자열이 나옴 > int로 변환이 안됨 > ValueError 발생

    result=sum(map(lambda s: int(s or 0), numbers.split('/'))) # or는 s가 거짓일때() 0으로 치환되서 처리
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))

#1. Function Based View 
# example1 HttpResponse
def post_list1(request):
    name = "헤이즈"
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))

# example2 template 사용하기
def post_list2(request):
    name='헤이즈'
    return render(request, 'dojo/post_list.html',{'name':name})

# exmple3 json형식
def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items' : ['파이썬','장고','Celery','Azure','AWS'],
    }, json_dumps_params={'ensure_ascii':True})
#     ensure_ascii=True일 때에는 유니코드 코드값으로 인코딩되고,
#     ensure_ascii=False일 때에는 utf8 인코딩으로 인코딩됩니다.

# exampl4 Excel 다운로드
def excel_download(request):
    # filepath = '/Users/giyeon/01Nomade/05django/01firstvod/src/example.xls'
    filepath = os.path.join(settings.BASE_DIR,'example.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # content_type지정 안해주면 'text/html', 엑셀타입 지정 application/vnd.ms-excel
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
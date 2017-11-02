# dojo/views.py
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

'''
def mysum(request,x,y=0,z=0): #y=0,z=0으로 default 값을 지정해준다.
#view함수는 클라이언트가 서버로 넘길때, 첫번째 인자는 무조건 request를 받는다.
#request: HttpRequest 는 request의 인스턴스
    return HttpResponse(int(x)+int(y)+int(z))
'''

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
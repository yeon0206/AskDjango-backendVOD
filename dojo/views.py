# dojo/views.py
from django.http import HttpResponse
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
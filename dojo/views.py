# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request,x,y=0,z=0): #y=0,z=0으로 default 값을 지정해준다.
#view함수는 클라이언트가 서버로 넘길때, 첫번째 인자는 무조건 request를 받는다.
#request: HttpRequest 는 request의 인스턴스
    return HttpResponse(int(x)+int(y)+int(z))

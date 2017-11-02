# blog/urls.py
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list),
]

#정규표현식: ^: 문자열의 시작, $: 문자열의 끝, 따라서 아무런 문자열이 없다, 즉, 최상위 주소 패턴을 의미한다.
#views에 post_list 함수 자체를 넘겨준다. 파이썬은 1급함수를 지원하는 언어이기때문에, 함수를 인자로써 넘겨 줄 수 있다.
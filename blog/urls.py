# blog/urls.py
from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'), # 포스팅 목록
    url(r'^$', views_cbv.post_list, name='post_list'), # 포스팅 목록(CBV)
    
    url(r'^new/$', views.post_new, name='post_new'), # 새 포스팅
    # url(r'^cbv/new/$', views_cbv.post_new, name='post_new'), # 새 포스팅 (CBV)
    
    # url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'), # 포스팅 보기(post_detail일 함수는 id라는 이름의 필드를 받을수 있어야한다)
    url(r'^(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'), # 포스팅 보기(CBV)

    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'), # 포스팅 수정
    # url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'), # 포스팅 수정(CBV)
    
    # url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='post_delete'), # 포스팅 삭제(구현안함)
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'), # 포스팅 삭제(CBV)
    
    url(r'^comments/$', views.comment_list, name='comment_list'), #

    # url(r'^(?P<id>\d+)/comments/$', views.comment_list, name='comment_list'), # 댓글 목록
    # url(r'^(?P<post_id>\d+)/comments/(?P<id>\d+)/edit/$', views.comment_edit, name='comment_edit'),# 댓글 수정
    # url(r'^(?P<post_id>\d+)/comments/(?P<id>\d+)/delete/$', views.comment_delete, name='comment_delete'),# 댓글 삭제
]

#정규표현식: ^: 문자열의 시작, $: 문자열의 끝, 따라서 아무런 문자열이 없다, 즉, 최상위 주소 패턴을 의미한다.
#views에 post_list 함수 자체를 넘겨준다. 파이썬은 1급함수를 지원하는 언어이기때문에, 함수를 인자로써 넘겨 줄 수 있다.
#List 는 순서가 있는 자료구조
#요청이 들어오면 순서대로 url맵핑한다. 맵핑되면 return으로 url을 줌.

# (?P ) : 이 영역의 문자열에 정규표현식을 적용해서
# \d+ : \d+ 패턴에 부합된다면
# <x> : x 라는 변수명으로 인자를 넘기겠다.

# 뷰의 인자로 넘겨받은 값들은 모두 문자열 타입입니다.
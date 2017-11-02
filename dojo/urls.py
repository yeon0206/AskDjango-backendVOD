#dojo/urls.py
from django.conf.urls import url
from . import views
from . import views_cbv
'''
urlpatterns =[
    url(r'^sum/(?P<x>\d+)/$', views.mysum), #숫자를 하나만 받기
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum), #숫자를 두개 받기
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum), #숫자를 세개 받기
]
'''

urlpatterns =[
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
        #[\d/]+ : 숫자혹은 /가 하나이상 반복이된다면

    #/hello/공유/37/ 응답으로서 "안녕하세요. 공유. 37살이시네요."    
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1), 
    url(r'^cbv/list2/$', views_cbv.post_list2),
    url(r'^cbv/list3/$', views_cbv.post_list3),
    url(r'^cbv/excel/$', views_cbv.excel_download),
]
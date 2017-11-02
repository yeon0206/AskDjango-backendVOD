#dojo/urls.py
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^sum/(?P<x>\d+)/$', views.mysum), #숫자를 하나만 받기
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum), #숫자를 두개 받기
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum), #숫자를 세개 받기
]
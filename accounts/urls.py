from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views #장고 기본 views 함수를 가져다써서 로그인과,로그아웃을 바로 호출한다.
from .forms import LoginForm
from . import views
urlpatterns=[
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login',
        kwargs={
            'authentication_form' : LoginForm,
            'template_name':'accounts/login_form.html',
            }),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^profile/$', views.profile, name='profile'),
]


# settings의 티폴트값 : 
# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/accounts/profile/'

# 앱/urls.py 에 namespace를 지정하실 수도 있습니다.
# 앱에 일단 namespace를 적용하면, URL Reverse 시에는 필히 namespace를 써야만 합니다.
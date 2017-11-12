# accounts/views.py

from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm 기본내장->커스텀(Form을 만들어준다)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

from .forms import SignupForm, LoginForm

'''
기본내장 회원가입 로직
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # dafault : "/accounts/login"
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })
'''

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # dafault : "/accounts/login"
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

'''
체킹 루틴을 함수로 지정 가능
from django.contrib.auth.decorators import user_passes_test
@user_passes_test(lambda user: user.is_authenticated() and user.point > 50000)
def gold_membership(request):
 return render(request, 'app/gold_membership.html')
'''

def login(request):
    providers = []
    for provider in get_providers(): #settings/INSTALLED_APPS 내에서 활성화된 목록
    # social_app속성은 provider에는 없는 속성입니다. 템플릿에서 활용하기 위해 임의의 이름을 할당
        try:
            #실제 provider 별 Client id/secret이 등록 되어있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    return auth_login(request, #기본 login에 파라미터만 세팅, providers리스트만 만들어주면됨
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})
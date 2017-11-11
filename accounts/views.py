# accounts/views.py

from django.conf import settings
# from django.contrib.auth.forms import UserCreationForm 기본내장->커스텀(Form을 만들어준다)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import SignupForm

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
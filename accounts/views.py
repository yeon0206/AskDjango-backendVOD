# accounts/views.py

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

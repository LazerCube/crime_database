from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from accounts.models import User
from accounts.forms import AuthenticationForm, RegistrationForm

from django.http import HttpResponse

def register(request):
    if not request.user.is_authenticated():
        title = 'staff register'
        form = RegistrationForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.save()
            if user:
                return HttpResponse('REGISTED!!!')

        context = {
                'form': form,
                'title':title,
        }

        return render(request, 'accounts/base.html', context)
    else:
        return HttpResponse('You are already logged in')

def login(request):
    if not request.user.is_authenticated():
        form = AuthenticationForm(request.POST or None)
        title = 'login'
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                auth_login(request, user)
                return HttpResponse('Logged In!!')

        context = {
                'form': form,
                'title': title,
        }

        return render(request, 'accounts/base.html', context)
    else:
        return HttpResponse('You are already logged in')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

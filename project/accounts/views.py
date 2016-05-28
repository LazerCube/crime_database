from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from accounts.models import User
from accounts.forms import AuthenticationForm, RegistrationForm, EditForm


@login_required
def account(request):
    user = get_object_or_404(User,pk=request.user.pk)
    form = EditForm(request.POST or None, instance=user)
    if request.POST and form.is_valid():
        user = form.save()

    context = {
            'user': user,
            'form': form,
    }
    return render(request, 'accounts/view.html', context)

def register(request):
    if not request.user.is_authenticated():
        title = 'register'
        form = RegistrationForm(request.POST or None)
        if request.POST and form.is_valid():
            user = form.save()
            if user:
                return redirect('accounts:login')

        context = {
                'form': form,
                'title':title,
        }

        return render(request, 'accounts/base.html', context)
    else:
        return redirect('accounts:view')

def login(request):
    if not request.user.is_authenticated():
        form = AuthenticationForm(request.POST or None)
        title = 'login'
        if request.POST and form.is_valid():
            user = form.login(request)
            if user:
                print("USER")
                auth_login(request, user)
                return redirect('accounts:view')

        context = {
                'form': form,
                'title': title,
        }

        return render(request, 'accounts/base.html', context)
    else:
        return redirect('accounts:view')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

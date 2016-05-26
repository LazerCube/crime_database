from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from accounts.models import User
from accounts.forms import AuthenticationForm, RegistrationForm

from django.http import HttpResponse

def register(request):
    if not request.user.is_authenticated():
        title = 'register'
        form = RegistrationForm()

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = User.objects.create_user(email, password, username=username, first_name=first_name, last_name=last_name)
                return HttpResponse('New user created!!!!')

        context = {
                'form': form,
                'title':title,
        }

        return render(request, 'accounts/base.html', context)
    else:
        return HttpResponse('You are already logged in')

def login(request):
    if not request.user.is_authenticated():
        form = AuthenticationForm()
        state = ''
        title = 'login'
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                        return HttpResponse('Logged In!!')
                    else:
                        state = "Your account is not active, please contact the administrator."
                else:
                    state = "Your username and/or password were incorrect."

        context = {
                'state': state,
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

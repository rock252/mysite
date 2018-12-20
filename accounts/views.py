from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . forms import *
from django.contrib.auth import logout

def user_login(request):
    if request.user.is_authenticated():
        return redirect('customer_portal1')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'],password=cd['password'])
                if user is not None:
                    login(request, user)
                    return redirect('customer_portal1')
                else:
                    return redirect('first')
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
    
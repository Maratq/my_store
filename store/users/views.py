from django.shortcuts import render, reverse
from django.views import View
from users.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm
        return render(request, 'users/login.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/index')


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/register.html', context={
            'form': form,
        })

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'users/register.html', context={
            'form': form
        })

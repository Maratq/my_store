from django.shortcuts import render, reverse
from django.views import View
from .models import User
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from products.models import Basket
from django.contrib.auth.decorators import login_required


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
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login'))
        return render(request, 'users/register.html', context={
            'form': form
        })


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'users/profile.html', context={
        'title': 'Store - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    })

# def logout(request):
#   return HttpResponseRedirect(reverse('/index'))

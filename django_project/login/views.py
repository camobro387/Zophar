from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm, AuthenticationForm, UserCreationForm
from .forms import LoginForm, SignUpForm, AuthenticationForm
# Create your views here.


class Main(View):
    def get(self, request):
        return HttpResponse(render(request, 'login/index.html', {'form' : AuthenticationForm}))

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/main_page')

            else:
                # Return an 'invalid login' error message.
                return HttpResponseForbidden('wrong pass')
        else:
            return HttpResponse('bad')


class Create(View):
    def get(self, request):
        return HttpResponse(render(request, 'login/create.html', {'form' : SignUpForm}))

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main_page')
        else:
            return HttpResponse('error')

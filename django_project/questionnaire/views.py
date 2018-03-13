from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from .forms import QuestionForm

class Main(View):
    def get(self, request):
        return HttpResponse(render(request, 'login/index.html', {'form' : QuestionForm}))

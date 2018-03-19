from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from .forms import QuestionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Main(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse(render(request, 'questionnaire/index.html', {'form': QuestionForm}))

    def post(self, request):
        pass
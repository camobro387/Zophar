from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Main(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('response')

class CheckIn(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('response')

class View(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('response')

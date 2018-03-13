from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Main:
    def get(self, request):
        return HttpResponse('response')

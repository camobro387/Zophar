from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
# Create your views here.

class Main(LoginRequiredMixin, View):
    def get(self, request):
        # num_names = Pages.objects.all().count()
        # num_urls = Pages.objects.all().count()
        pages = Page.objects.all().order_by('order')
        return HttpResponse(render(request, 'main_page/index.html', {'pages': pages}))

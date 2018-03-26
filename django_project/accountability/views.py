from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from login.models import Profile
from .models import ChurchCheckIn, BibleReading
from .forms import BibleForm

import datetime

# Create your views here.


class Main(LoginRequiredMixin, View):
    def get(self, request):
        hours = self.time_read_in_week()
        self.get_data_for_user(request.user)
        form = BibleForm()
        context = {'hours_read': hours, 'form': form}
        context.update(self.get_data_for_user(request.user))
        print(context)
        return HttpResponse(render(request, 'accountability/index.html', context=context))

    def get_data_for_user(self, user):
        # User data from profile
        user_data = Profile.objects.filter(user=user)[0]

        # Last check in

        return {'reading_email': user_data.accountability_partner_reading,
                'church_email': user_data.accountability_partner_church,
                'reading_goal': user_data.reading_goal
                }
    #
    def time_read_in_week(self):
        """
        Searches the database for how much time the user has spent reading the bible this week.
        :return:
        """
        return 0


class Church(LoginRequiredMixin, View):
    def post(self, request):
        at_church = request.POST.get('slider')
        self.make_check_in(at_church, request.user)
        return redirect('/accountability')

    def make_check_in(self, at_church, user):
        if at_church == None: bool = False
        else: bool = True
        date = datetime.datetime.now()
        ChurchCheckIn.objects.create(
            check_in=bool,
            date=date,
            user=user)


class Reading(LoginRequiredMixin, View):
    def post(self, request):
        reading = request.POST.get('slider')
        return redirect('/main_page')

    def make_check_in(self, reading, user):
        if reading == None: bool = False
        else: bool = True
        date = datetime.datetime.now()
        ChurchCheckIn.objects.create(
            reading=bool,
            date=date,
            user=user)

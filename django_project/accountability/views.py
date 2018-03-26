from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from login.models import Profile
from .models import ChurchCheckIn, BibleReading
from .forms import SliderForm, DropdownForm

import datetime

# Create your views here.


class Main(LoginRequiredMixin, View):
    def get(self, request):
        hours = ReadingData(request.user).time_read_in_week()
        self.get_data_for_user(request.user)

        church_data = ChurchData(request.user)
        last_church_date = church_data.last_check_in()
        last_church_location = None

        slider_form = SliderForm()
        dropdown_form = DropdownForm()
        context = {
            'hours_read': hours,
            'last_church_date': last_church_date,
            'last_church_location': last_church_location,
            'slider_form': slider_form,
            'dropdown_form': dropdown_form
        }

        context.update(self.get_data_for_user(request.user))
        print(context)
        return HttpResponse(render(
            request,
            'accountability/index.html',
            context=context)
        )

    def get_data_for_user(self, user):
        # User data from profile
        user_data = Profile.objects.filter(user=user)[0]

        # Last check in

        return {'reading_email': user_data.accountability_partner_reading,
                'church_email': user_data.accountability_partner_church,
                'reading_goal': user_data.reading_goal
                }


class ChurchData():

    def __init__(self, user):
        self.user = user

    def last_check_in(self):
        q = ChurchCheckIn.objects.filter(user=self.user).order_by('-id')
        if len(q) == 0:
            return "No check ins! Go to church"
        else:
            d = q[0].date
            date = str(d.year) + ' ' + str(d.month) + ' ' + str(d.day)
            return date

class ReadingData():

    def __init__(self, user):
        self.user = user

    def time_read_in_week(self):
        """
        Searches the database for how much time the user has spent reading the bible this week.
        :return:
        """
        query = BibleReading.objects.filter(
            user=self.user
        ).filter(
            date__range=self.date_list()
        )
        total_hours = 0
        for reading in query:
            total_hours += reading.time_read

        return total_hours

    def date_list(self):
        '''
        Makes list of days since last Sunday.
        '''
        today = datetime.datetime.now()
        day = datetime.datetime.weekday(today)
        today = datetime.date(today.year, today.month, today.day)
        last_sunday = today.day - day - 1
        last_sunday = datetime.date(today.year, today.month, last_sunday)
        return [last_sunday, today]


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
        reading = request.POST.get('dropdown')
        entry = BibleReading(
            time_read=reading,
            date=datetime.date.today(),
            user=request.user
        )
        entry.save()
        return redirect(reverse('accountability'))

    def make_check_in(self, reading, user):
        if reading == None: bool = False
        else: bool = True
        date = datetime.datetime.now()
        ChurchCheckIn.objects.create(
            reading=bool,
            date=date,
            user=user)

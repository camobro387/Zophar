import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View

from login.models import Profile
from .forms import SliderForm, DropdownForm
from .models import ChurchCheckIn, BibleReading


class Main(LoginRequiredMixin, View):
    def get(self, request):
        self.user = request.user

        hours = ReadingData(self.user).time_read_in_week()
        self.get_data_for_user()

        church_data = ChurchData(self.user)
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

        context.update(self.get_data_for_user())
        print(context)
        return HttpResponse(render(
            request,
            'accountability/index.html',
            context=context)
        )

    def get_data_for_user(self):
        # User data from profile
        user_data = Profile.objects.filter(user=self.user)[0]

        # Last check in

        return {'reading_email': user_data.accountability_partner_reading,
                'church_email': user_data.accountability_partner_church,
                'reading_goal': user_data.reading_goal
                }


class ChurchData:
    """
    Used to query the db and format data
    """

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


class ReadingData:

    def __init__(self, user):
        self.user = user

    def time_read_in_week(self):
        """
        Searches the database for how much time the user has spent reading the bible this week.

        :return: total number of hours read in the last week.
        """
        query = BibleReading.objects.filter(
            user=self.user
        ).filter(
            date__range=self.date_range()
        )
        total_hours = 0
        for reading in query:
            total_hours += reading.time_read

        return total_hours

    @staticmethod
    def date_range():
        """
        Makes list of days since last Sunday.

        Will not currently work if week split between this month and end of last month.

        :return: a list with two entries. The first is the date of the last Sunday, the first is today's date.
        """
        today = datetime.datetime.now()
        day = datetime.datetime.weekday(today)
        today = datetime.date(today.year, today.month, today.day)
        last_sunday = today.day - day - 1  # Adjust by -1 because datetime.weekday uses Monday as index 0.
        last_sunday = datetime.date(today.year, today.month, last_sunday)
        return [last_sunday, today]


class Church(LoginRequiredMixin, View):
    def post(self, request):
        at_church = request.POST.get('slider')
        self.make_check_in(at_church, request.user)
        return redirect('/accountability')

    @staticmethod
    def make_check_in(at_church, user):
        if at_church is None:
            church_b = False
        else:
            church_b = True
        date = datetime.datetime.now()
        ChurchCheckIn.objects.create(
            check_in=church_b,
            date=date,
            user=user)


class Reading(LoginRequiredMixin, View):
    def post(self, request):
        self.user = request.user

        reading = request.POST.get('dropdown')
        entry = BibleReading(
            time_read=reading,
            date=datetime.date.today(),
            user=self.user
        )
        entry.save()
        return redirect(reverse('accountability'))

    def make_check_in(self, reading):
        if reading is None:
            read_b = False
        else:
            read_b = True
        date = datetime.datetime.now()
        ChurchCheckIn.objects.create(
            reading=read_b,
            date=date,
            user=self.user)

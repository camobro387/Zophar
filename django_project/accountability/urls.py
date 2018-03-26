from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Main.as_view()),
    url(r'^checkin/church/$', views.Church.as_view(), name='church'),
    url(r'^checkin/read/$', views.Reading.as_view(), name='read')
]

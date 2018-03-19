from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout
urlpatterns = [
    url(r'^$', views.Main.as_view()),
    url(r'^create/$', views.Create.as_view()),
    url(r'^logout/$', logout, {'next_page': '/login'}),
]
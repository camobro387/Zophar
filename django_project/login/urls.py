from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Main.as_view()),
    url(r'^create/$', views.Create.as_view()),
]
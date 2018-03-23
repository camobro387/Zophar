from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.Main.as_view())
]
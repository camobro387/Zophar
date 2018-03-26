"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls'), name='login'),
    path('accountability/', include('accountability.urls'), name='accountability'),
    path('encouragement/', include('encouragement.urls'), name='encouragement'),
    path('', include('main_page.urls'), name='main_page'),
    path('questionnaire/', include('questionnaire.urls'), name='questionnaire'),
    path('settings/', include('settings.urls'), name='settings'),
    path('small_group/', include('small_group.urls'), name='small_group'),
    path('ways_to_serve/', include('ways_to_serve.urls'), name='ways_to_serve'),
]


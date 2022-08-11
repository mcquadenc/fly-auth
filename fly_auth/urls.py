"""fly_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import index
import debug_toolbar
# from django.contrib.auth.views import login
from fake_user.views import login, logout



urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', login, name="v_login"),
    url(r'^logout/$', logout, name="v_logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'__debug__/', include(debug_toolbar.urls)),
]

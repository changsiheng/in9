#coding:utf-8
"""django_08day13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from app01 import views
from django.conf.urls import url
from django.contrib import admin
from app02 import views as app02_views
from app03 import views as app03_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/(\d*)', views.index),#后边可以加数字
    url(r'^app02/login/',app02_views.login),
    url(r'^app02/index/',app02_views.index),
    url(r'^app03/index/',app03_views.home)
    
]

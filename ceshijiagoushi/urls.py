# -*- coding: utf-8 -*-
"""ceshijiagoushi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from testing import views #导入testing应用views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index), #访问http://127.0.0.1:8001/默认跳转到登录页面
    url(r'^index/$', views.index),  #添加index/路径配置,访问http://127.0.0.1:8001/index/默认跳转到登录页面
    url(r'^accounts/login/$', views.index), #访问http://127.0.0.1:8001/event_manage/默认跳转到登录页面
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
]

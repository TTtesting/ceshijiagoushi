# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    #return HttpResponse("Hello ceshijiagoushi!")
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password) #使用authenticate()函数认证给出的用户名和密码
        if user is not None:
        #if username == 'admin' and password == 'admin123':
            auth.login(request, user) #登录
            #return HttpResponseRedirect('/event_manage/')
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user', username, 3600) #添加浏览器cookie
            request.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required #限制event_manage目录下必须登录后才能访问
def event_manage(request):
    #username = request.COOKIES.get('user', '') #读取浏览器cookie
    username = request.session.get('user', '') #读取浏览器session
    return render(request,"event_manage.html",{"user":username})
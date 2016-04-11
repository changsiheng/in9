#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect

# Create your views here.

#@csrf_protect   指定跨站请求约束，可以
def login(request):
    
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user == 'alex' and pwd =='123':
            request.session['is_login'] = {'username':user}
            return redirect('/app02/index/')
        else:
            return render_to_response('app02/login.html',{'msg':'用户名密码错误'},context_instance=RequestContext(request))
    

    
    return render_to_response('app02/login.html',context_instance=RequestContext(request))

def index(request):
    user_dict = request.session.get('is_login',None)
    if user_dict:
        return render_to_response('app02/index.html',{'username':user_dict['username']})
    else:
        return redirect('/app02/login/')
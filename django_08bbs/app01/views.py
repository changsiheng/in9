from django.shortcuts import render,render_to_response,HttpResponse,redirect
from app01 import models
import json
from django.core import serializers
from django.db.models.query import QuerySet
import datetime
from jsonpickle.tags import NEWOBJ
from cherrypy import request


# Create your views here.

def login(request):
    
    if request.method == 'POST':
    
        username = request.POST.get('username')
        
        password = request.POST.get('password')
        
        try:
            currentObj = models.Admin.objects.get(username=username,password=password)
        except Exception,e:
            currentObj = None
            
        if currentObj:
            request.session['current_user_id'] = currentObj.id
            return redirect('/index/')
        else:
            render_to_response('login.html')
    return render_to_response('login.html')

def index(request):
    
    all_data = models.News.objects.all()
    
    return render_to_response('index.html',{'data':all_data})


def addfavor(request):
    ret = {'status':0,'data':'','message':''}
    try:
        
        id = request.POST.get('nid')
        newsObj = models.News.objects.get(id=id)
        temp = newsObj.favor_count + 1
        newsObj.favor_count = temp
        newsObj.save()
        ret['status']=1
        ret['data'] = temp
        
    except Exception,e:
        ret['message']=e.message
    
    return HttpResponse(json.dumps(ret))

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M;%S')
        elif isinstance(obj,date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
        


def getreply(request):
    id = request.POST.get('nid')
    reply_list = models.Reply.objects.filter(new__id=id).values('id','content','create_date','user__username')
    reply_list = list(reply_list)
    reply_list = json.dumps(reply_list,cls=CJsonEncoder)
    #print reply_list
    return HttpResponse(reply_list)


def submitreply(request):
    
    #request.session['current_user_id'] = 1
    ret = {'status':0,'data':'','message':''}
    try:
        nid =  request.POST.get('nid')
        data =  request.POST.get('data')
        userid = request.session['current_user_id']
        newsObj = models.News.objects.get(id=nid)
        obj = models.Reply.objects.create(content = data,
                                    user = models.Admin.objects.get(id=userid),
                                    new = newsObj)
        temp = newsObj.reply_count + 1
        newsObj.reply_count=temp
        newsObj.save()
        ret['data'] = {'reply_count':temp,'content':obj.content,'user__username':obj.user.username,'create_date':obj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
        ret['status']=1
    except Exception,e:
        
        ret['message']=e.message
        
    return HttpResponse(json.dumps(ret))
        
        

def submitchat(request):
    ret = {'status':0,'data':'','message':''}
    try:
        value = request.POST.get('data')
        userObj = models.Admin.objects.get(id=request.session['current_user_id'])
        chatObj = models.Chat.objects.create(content=value,user=userObj)
        ret['status']=1
        ret['data']={'id':chatObj.id,'username':userObj.username,'create_data':chatObj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
    except Exception,e:
        ret['message']=e.message
        
    return HttpResponse(json.dumps(ret))

def getchart(request):
    chatList = models.Chat.objects.all().order_by('-id')[0:10].values('id','content','user__username','create_date')
    chatList = list(chatList)
    chatList = json.dumps(chatList,cls=CJsonEncoder)
    return HttpResponse(chatList)

def getchar2(request):
    last_id = request.POST.get('lastid')
    chatList = models.Chat.objects.filter(id__gt=last_id).values('id','content','user__username','create_date')
    chatList = list(chatList)
    chatList = json.dumps(chatList,cls=CJsonEncoder)
    return HttpResponse(chatList)
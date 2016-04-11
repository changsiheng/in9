#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,render_to_response
from app01 import models
from app01 import common
from django.utils.safestring import mark_safe
# Create your views here.
from app01 import htmlhelper
def index(request,page):
    #操作数据库，进行分页
    #第一页0-4 page = 1 
    #第二页5-10 page = 2
    #第三页10-15 page = 3
    #(page-1)*5 page*5
    #per_item = common.try_int(request.COOKIES.get('pager_num',10),10)
    per_item = common.try_int(request.COOKIES.get('pager_num',None),10)
    print per_item
    page = common.try_int(page, 1)
    #page = int(page)
    count = models.Host.objects.all().count()
    '''
    per_item = 5
    start = (page-1)*per_item
    end = (page*per_item)
    temp = divmod(count, per_item)
    if temp[1]==0:
        all_page_count = temp[0]
    else:
        all_page_count = temp[0]+1
    '''
    
    
    pageObj = htmlhelper.PageInfo(page,count,per_item)
    result = models.Host.objects.all()[pageObj.start:pageObj.end]
    
    
    '''
    page_html = []
    first_html = "<a href='/index/%d'>首页</a>" %(1,)
    page_html.append(first_html)
    
    if page <= 1:
        prev_html = "<a href='#'>上一页</a>"
    else:
        prev_html = "<a href='/index/%d'>上一页</a>" %(page-1,)
    
    page_html.append(prev_html)
    
    
    for i in range(all_page_count):
        if page == i+1:
            a_html = "<a class = 'selected' href='/index/%d'>%d</a>" %(i+1,i+1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" %(i+1,i+1)
        
        page_html.append(a_html)
    
    next_page = "<a href='/index/%d'>下一页</a>" %(page+1,)
    page_html.append(next_page)
    
    last_html = "<a href='/index/%d'>尾页</a>" %(all_page_count,)
    page_html.append(last_html)
    page = mark_safe(''.join(page_html))
    '''
    page_string = htmlhelper.Pager(page, pageObj.all_page_count)
    ret = {'data':result,'count':count,'page':page_string,'list':'10'}
    response = render_to_response('index.html',ret)
    
    response.set_cookie('pager_num',per_item) #设置COOKIE
    
    return response
#!/usr/bin/env python
#coding:utf-8
'''
Created on Apr 4, 2016

@author: root
'''
from django.shortcuts import render,render_to_response
from app01 import models
from app01 import common
from django.utils.safestring import mark_safe

class PageInfo:
    def __init__(self,current_page,all_count,per_item=5):
        self.CurrentPage = current_page
        self.Allcount = all_count
        self.perItem = per_item
    @property    
    def start(self):
        #start = (page-1)*per_item
        return (self.CurrentPage-1)*self.perItem
    @property
    def end(self):
        #end = (page*per_item)
        return self.CurrentPage * self.perItem
    @property
    def all_page_count(self):
        '''
        temp = divmod(count, per_item)
        if temp[1]==0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0]+1
        '''
        temp = divmod(self.Allcount,self.perItem)
        if temp[1]==0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0]+1
            
        return all_page_count
            
def Pager(page,all_page_count):
    '''
    page:表示当前页
    all_page_count:表示的是总页数
    '''
    page_html = []
    first_html = "<a href='/index/%d'>首页</a>" %(1,)
    page_html.append(first_html)
    
    if page <= 1:
        prev_html = "<a href='#'>上一页</a>"
    else:
        prev_html = "<a href='/index/%d'>上一页</a>" %(page-1,)
    
    page_html.append(prev_html)
    
    begin = page - 6
    end = page + 5
    if all_page_count < 11:
        begin = 0
        end = all_page_count
    else:
        if page < 6:
            begin=0
            end =11
        else:
            if page + 6 > all_page_count:
                begin = page-6
                end = all_page_count
            else:
                begin = page - 6
                end = page + 5
    #for i in range(all_page_count):
    for i in range(begin,end):    
        if page == i+1:
            a_html = "<a class = 'selected' href='/index/%d'>%d</a>" %(i+1,i+1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" %(i+1,i+1)
        
        page_html.append(a_html)
    if page >= all_page_count:
        next_page = "<a href='#'>下一页</a>"
    else:
        next_page = "<a href='/index/%d'>下一页</a>" %(page+1,)
    
    page_html.append(next_page)
    
    last_html = "<a href='/index/%d'>尾页</a>" %(all_page_count,)
    page_html.append(last_html)
    
    page_string = mark_safe(''.join(page_html))
    
    return page_string
    
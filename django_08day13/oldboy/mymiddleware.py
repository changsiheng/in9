#!/ysr/bin/env python
#coding:utf-8
'''
Created on Apr 9, 2016

@author: root
'''
from django.http.response import HttpResponse
from cherrypy import request

class Day13Middleware(object):
    
    def process_request(self,request):
        print '1.process_request'
        print '404'
        return HttpResponse('404 Not found')
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print '1.process_view'
        
    def process_exception(self,request,exception):
        print '1.process_exception'
        
    def process_response(self,request,response):
        print '1.process_response'
        return response

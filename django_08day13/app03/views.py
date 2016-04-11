#!/usr/bin/env python
#coding:utf-8
from __future__ import unicode_literals
 
import json
from django.shortcuts import render,render_to_response
 
def home(request):
    return render_to_response('app03/home.html')
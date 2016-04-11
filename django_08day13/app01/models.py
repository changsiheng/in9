#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Host(models.Model):
    HostName = models.CharField(max_length=256)
    IP = models.IPAddressField
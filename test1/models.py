# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)
    username = models.CharField(max_length=100)

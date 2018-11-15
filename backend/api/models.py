# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here. create database here
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' - ' + self.password + ' - ' + self.email

class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=60, default='SOME STRING')

    def __str__(self):
        return self.field_name
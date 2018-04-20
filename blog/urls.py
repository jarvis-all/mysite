#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: William Fu

from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('<int:blog_pk>',views.blog_detail,name='blog_detail'),
    path('type/<int:blog_type_pk>',views.blog_with_type,name='blog_with_type'),
    path('',views.blog_list,name='blog_list'),
]

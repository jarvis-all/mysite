#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: William Fu
from django.shortcuts import render_to_response

def Home(request):
    context = {}
    return render_to_response('index.html',context)
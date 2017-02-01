#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Thejojo'

from django.conf.urls import url,include
from lists.views import view_list
from lists.views import new_list
from lists.views import register
from lists.views import userinfo
from lists import views as lists_views

urlpatterns = [
    url(r'^(\d+)/$', view_list, name="view_list"),
    url(r'^new$', new_list, name="new_list"),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/register',register, name="register"),
    url(r'^accounts/userinfo',userinfo, name="userinfo"),


]
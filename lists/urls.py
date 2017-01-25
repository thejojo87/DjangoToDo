#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Thejojo'

from django.conf.urls import url
from lists.views import view_list
from lists.views import new_list
from lists.views import add_item
from lists import views as lists_views

urlpatterns = [
    url(r'^(\d+)/$', view_list, name="view_list"),
    url(r'^(\d+)/add_item$', add_item, name="add_item"),
    url(r'^new$', new_list, name="new_list"),
]
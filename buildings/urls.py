#!/usr/bin/env python3

from django.urls import path

from .views import *

urlpatterns = [
    path("list/", building_list, name="list"),
    path("select/", building_options, name="select"),
    path("", page, name="page"),
]

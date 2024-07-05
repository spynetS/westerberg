#!/usr/bin/env python3

from django.urls import include, path

from .views import *

urlpatterns = [
    path("", main, name=""),
    path("lokal/", lokal, name=""),
]

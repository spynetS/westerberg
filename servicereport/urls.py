#!/usr/bin/env python3


from django.urls import path

from .views import create_report, getform

urlpatterns = [
    path("createreport/", create_report, name="list"),
    path("getform/", getform, name="getform"),
]

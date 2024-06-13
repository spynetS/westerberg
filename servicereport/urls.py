#!/usr/bin/env python3


from django.urls import path

from .views import *

urlpatterns = [
    path("createreport/", create_report, name="list"),
]

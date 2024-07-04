#!/usr/bin/env python3

from django.urls import include, path

from .views import SignUpView
from .views import intrestreport

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("intrestreport/", intrestreport, name="signup"),
]

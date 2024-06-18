#!/usr/bin/env python3

from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", views.admin, name="admin"),
    path("select/", views.page, name="select"),
    path("rental/<str:adress>", views.rental_adress, name="rental"),
]

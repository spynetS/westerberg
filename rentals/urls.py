#!/usr/bin/env python3

from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", views.admin, name="admin"),
    path("rental/<str:adress>", views.rental_adress, name="rental"),
]

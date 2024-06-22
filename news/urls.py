#!/usr/bin/env python3
from django.urls import include, path

from . import views

urlpatterns = [
    path("create/", views.create_news, name="create"),
    path("edit/", views.edit, name="create"),
    path("delete/", views.delete, name="create"),
    path("page", views.page, name="page"),
    path("cards/", views.cards, name="cards"),
]

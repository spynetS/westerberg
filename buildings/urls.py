#!/usr/bin/env python3

from django.urls import path

from .views import *

urlpatterns = [
    path("list/", building_list, name="list"),
    path("select/", building_options, name="select"),
    path("select_areas/", select_areas, name="select"),
    path("select_areas/with_all", select_areas_with_all, name="select"),
    path("select_cities/", select_cities, name="select"),
    path("", main, name="page"),
    path("delete/", delete, name="delete"),
    path("building/<str:adress>", building_adress, name="rental"),
]

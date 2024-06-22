#!/usr/bin/env python3

from django.urls import include, path

from . import views

def lokaler(request):
    return views.page(request,True)

urlpatterns = [
    path("admin/", views.admin, name="admin"),
    path("select/", views.page, name="select"),
    path("select/lokaler/", lokaler, name="select"),
    path("rental/<str:adress>/<int:pk>", views.rental_adress, name="rental"),
]

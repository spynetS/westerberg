#!/usr/bin/env python3

from django.urls import include, path

from . import views

def lokaler(request):
    return views.page(request,True)

urlpatterns = [
    path("setpublic/<int:pk>/",views.set_public),
    path("create/rental",views.create_rental),
    path("delete/",views.delete),
    path("create/lokal",views.create_lokal),
    path("admin/", views.admin, name="admin"),
    path("select/", views.page, name="select"),
    path("select/lokaler/", lokaler, name="select"),
    path("rental/<str:adress>/<int:pk>", views.rental_adress, name="rental"),
]

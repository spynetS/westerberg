#!/usr/bin/env python3


import time
from django.db.models import options
from django.shortcuts import render

from .models import Building


def building_list(request):
    if "select" in request.GET:
        buildings = Building.objects.filter(area=request.GET['select'])
    else:
        buildings = Building.objects.all()
    return render(request, "buildings/list.html",{"buildings": buildings})

def building_options(request):
    options = Building.City.choices
    print(options[0][1])
    options = [[i[0],i[1]] for i in options]
    return render(request, "buildings/select.html", {"options":options})

def page(request):
    if "select" in request.GET and request.GET["select"] != "alla":
        buildings = Building.objects.filter(city=request.GET['select'])
    else:
        buildings = Building.objects.all()

    sorted_buildings = {}
    for building in buildings:
        key = str(building.area) + "-id"
        print(sorted_buildings)
        if key not in sorted_buildings :
            print("new key")
            sorted_buildings[key] = [building]
        else :
            print("add")
            sorted_buildings[key].append(building)

    print(sorted_buildings)

    options = Building.City.choices
    options = [[i[0],i[1]] for i in options]

    return render(request, "buildings/page.html",{"buildings": list(sorted_buildings.values()),"options":options})

def fast(request):
    if "refresh" in request.headers:
        return page(request)
    if "select" in request.GET:
        return render(request, "fastigheter.html",{"select":"?select="+request.GET['select']})
    else:
        return render(request, "fastigheter.html",{})

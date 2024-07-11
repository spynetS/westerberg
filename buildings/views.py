#!/usr/bin/env python3


import time
from django.db.models import options
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render

from buildings.models import Images

from rentals.models import Rental

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
        select = request.GET["select"]
        buildings = Building.objects.filter(city=request.GET['select'])
    else:
        select = "alla"
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

    return render(request, "buildings/page.html",{"buildings": list(sorted_buildings.values()),"options":options,"select":select})


def fast(request):
    if "refresh" in request.headers:
        return page(request)
    if "select" in request.GET:
        return render(request, "fastigheter.html",{"select":"?select="+request.GET['select']})
    else:
        return render(request, "fastigheter.html",{})

def building_adress(request, adress):

    try:
        building = Building.objects.get(adress=adress)
    except:
        return HttpResponseNotFound()
    rentals = Rental.objects.filter(building=building,public=True)

    images = []
    for img in building.images.all():
        print(img.image.url)
        images.append([img.image.url,f"slide imge"])

    return render(request, "buildings/building.html",{"building":building,"images":images,"rentals":rentals})

def select_areas(request):
    return render(request,  "buildings/select.html",{"areas":Building.get_area_list()})

def select_areas_with_all(request):
    areas = Building.get_area_list()
    areas.insert(0,(0,'Alla'))
    return render(request,  "buildings/select.html",{"areas":areas})

def select_cities(request):
    return render(request,  "buildings/select_city.html",{"cities":Building.get_city_list()})

def delete(request):
    if request.method == "POST":
        try:
            building = Building.objects.get(pk=request.POST["pk"])
            building.delete()
            return render(request,"components/Alert.html",{"type":"success","msg":"Byggnaden togsbort"})
        except:
            return render(request,"components/Alert.html",{"type":"error","msg":"något gick fel!"})
    return HttpResponseNotFound()



def main(request):
    try:
        if request.method == "POST":
            for item in request.POST:
                if request.POST[item] == "":
                    return render(request,"components/Alert.html",{"type":"error","msg":"Fyll i alla fält!"})

            building = Building(
                adress=request.POST['adress'],
                city=request.POST['select_cities'],
                area=request.POST['select_areas'],
                description=request.POST['description'],
                lon=request.POST['lon'],
                lat=request.POST['lat'],
            )
            building.save()

            files = request.FILES.getlist('images')

            for file in files:
                image = Images(image=file)
                image.save()
                building.images.add(image)

            return render(request,"components/Alert.html",{"type":"success","msg":"Byggnaden lades till"})
        return page(request)
    except Exception as e:
        return render(request,"components/Alert.html",{"type":"error","msg":"Något gick fel! "+str(e)})

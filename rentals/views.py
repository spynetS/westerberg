from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from buildings.models import Building
from rentals.models import Rental
import json

# Create your views here.

def admin(request):
    return render(request,'rentals/admin.html',{"buildings":Building.objects.all()})

def rental_adress(request, adress,pk):
    try:
        rental = Rental.objects.get(building__adress=adress,pk=pk)
        rental.rent = rental.rent;
        rental.features = json.loads(rental.features)

        images = []
        for img in rental.building.images.all():
            print(img.image.url)
            images.append(img.image.url)

        return render(request,'rentals/rental.html',{"rental":rental,"images":images})
    except:
        return HttpResponseNotFound()

def page(request, lokaler=False):
    if "lokaler" in request.headers:
        lokaler = request.headers["lokaler"]

    if "select" in request.GET and request.GET["select"] != "alla":
        rentals = Rental.objects.filter(building__city=request.GET['select'],lokal=lokaler)
    else:
        rentals = Rental.objects.filter(lokal=lokaler)


    sorted_rentals = {}
    for rental in rentals:
        key = str(rental.building.area) + "-id"
        print(sorted_rentals)
        if key not in sorted_rentals :
            print("new key")
            sorted_rentals[key] = [rental]
        else :
            print("add")
            sorted_rentals[key].append(rental)

    print(sorted_rentals)

    options = Building.City.choices
    options = [[i[0],i[1]] for i in options]

    return render(request, "rentals/page.html",{"rentals": list(sorted_rentals.values()),"options":options,"lokaler":lokaler})

def ledigt(request):
    if "refresh" in request.headers:
        return page(request)
    if "select" in request.GET:
        return render(request, "ledigt.html",{"select":"?select="+request.GET['select'], "lokaler":False})
    else:
        return render(request, "ledigt.html",{"lokaler":False})

def ledigt_lokaler(request):
    if "refresh" in request.headers:
        return page(request,True)
    if "select" in request.GET:
        return render(request, "ledigt.html",{"select":"?select="+request.GET['select'], "lokaler":True})
    else:
        return render(request, "ledigt.html",{"lokaler":True})

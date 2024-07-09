from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.views.decorators.http import require_POST

from buildings.models import Building
from rentals.models import Rental
import json

# Create your views here.

def admin(request):
    return render(request,'rentals/admin.html',{"buildings":Building.objects.all()})

def rental_adress(request, adress,pk):
    try:
        rental = Rental.objects.get(building__adress=adress,pk=pk,public=True)
        rental.rent = rental.rent;
        rental.features = rental.features.split(",")

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
        rentals = Rental.objects.filter(building__city=request.GET['select'],lokal=lokaler,public=True)
    else:
        rentals = Rental.objects.filter(lokal=lokaler,public=True)


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

def create_annons(request,lokal):
    available_from_str = request.POST["available_from"]
    available_from_date = datetime.strptime(available_from_str, "%Y-%m-%d").date()

    rental = Rental(
        building=Building.objects.get(pk=request.POST["select_building"]),
        size=request.POST["size"],
        rooms=request.POST["rooms"],
        description=request.POST["description"],
        rent=request.POST["rent"],
        features=request.POST["features"],
        available_from=available_from_date,
        lokal = lokal,
        lokal_type = request.POST["select_lokal_type"] if lokal else Rental.LokalType.OVRIGT
    )
    rental.save()
    return rental;

def create_rental(request):
    if request.method == "POST":
        try:
            create_annons(request,False)
            return render(request, "components/Alert.html",{"type":"success","msg":"Annons tillagged"})
        except:
            return render(request, "components/Alert.html",{"type":"error","msg":"Något gick fel"})

    return HttpResponseNotFound()

def create_lokal(request):
    if request.method == "POST":
        try:
            create_annons(request,True)
            return render(request, "components/Alert.html",{"type":"success","msg":"Annons tillagged"})
        except:
            return render(request, "components/Alert.html",{"type":"error","msg":"Något gick fel"})

    return HttpResponseNotFound()

@require_POST
def delete(request):
    rental = get_object_or_404(Rental,pk=request.POST["pk"])
    rental.delete()
    return render(request, "components/Alert.html",{"type":"success","msg":"Annonsen är nu bortagen"})


@require_POST
def set_public(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    is_public = request.POST.get('is_public') == 'on'
    rental.public = is_public
    rental.save()
    return render(request, "components/Alert.html",{"type":"success","msg":"Annons är nu " + ("synlig" if rental.public else "osynlig")})

from django.shortcuts import render

from buildings.models import Building
from rentals.models import Rental
import json

# Create your views here.

def admin(request):
    return render(request,'rentals/admin.html',{"buildings":Building.objects.all()})

def rental_adress(request, adress):
    rental = Rental.objects.all()[0]
    rental.rent = rental.rent/100;
    print(rental.features)
    rental.features = json.loads(rental.features)
    print(rental.features)

    return render(request,'rentals/rental.html',{"rental":rental})

from django.shortcuts import render
from buildings.models import Building
from django.core.mail import send_mail
import urllib.parse

from intrestreport.models import IntrestReport
from rentals.models import Rental

# Create your views here.
def main(request):
    cities = Building.get_city_list()
    if request.method == "PUT":
        # if request.body.get("name") == "" or \
        #    request.body.get("personal_number")  == "" or \
        #    request.body.get("adress")  == "" or \
        #    request.body.get("employment")  == "" or \
        #    request.body.get("email")  == "" or \
        #    request.body.get("phone")  == "":
        #     return render(request, "intrestreport/bostad.html",{"error":"Fyll i de behövliga","cities":cities})
        raw_data = request.body.decode('utf-8')
        data = urllib.parse.parse_qs(raw_data)
        # Flatten the lists in the parsed data
        data = {k: v[0] for k, v in data.items()}

        report = IntrestReport(data=str(data))
        report.save()

        return render(request, "intrestreport/bostad.html",{"success":True,"cities":cities})
    return render(request, "intrestreport/bostad.html",{"cities":cities})


def lokal(request):
    cities = Building.get_city_list()
    lokaler = Rental.get_lokaltype_list()
    if request.method == "POST":
        for item in request.POST:
            if item != 'other' and request.POST[item] == "":
                return render(request, "intrestreport/lokal.html",{"error":"Fyll i alla fält'","cities":cities,"lokaler":lokaler})

        return render(request, "intrestreport/lokal.html",{"success":True,"cities":cities,"lokaler":lokaler})


    return render(request, "intrestreport/lokal.html",{"cities":cities,"lokaler":lokaler})

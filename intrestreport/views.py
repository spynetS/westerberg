from django.template.loader import render_to_string
from westerberg import settings
from django.shortcuts import render
from buildings.models import Building
from django.core.mail import EmailMessage, send_mail

import urllib.parse

from intrestreport.models import IntrestReport
from rentals.models import Rental

# Create your views here.
def main(request):
    cities = Building.get_city_list()
    if request.method == "POST":
        if request.POST["name"] == "" or \
           request.POST["personal_number"]  == "" or \
           request.POST["adress"]  == "" or \
           request.POST["employment"]  == "" or \
           request.POST["email"]  == "" or \
           request.POST["phone"]  == "":
            return render(request, "intrestreport/bostad.html",{"error":"Fyll i de behövliga","cities":cities})


        data = request.POST.copy()
        selected_city_values = request.POST.getlist('city')
        selected_city_labels = [Building.City(value).label for value in selected_city_values]
        print(selected_city_labels)

        data['city'] = selected_city_labels

        data['area'] = Building.Area(request.POST['select_areas']).label if data['select_areas'] != '0' else "Alla"

        body = render_to_string("intrestreport/intrestreport_mail.html",context=data,request=request)

        email = EmailMessage(
            f'Serviceanmälan {data["area"]}',
            body,
            settings.EMAIL_HOST_USER,
            [settings.INTRESTREPORT_EMAIL],
        )
        email.content_subtype = "html"  # Ensure the email content type is set to HTML
        email.send()

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

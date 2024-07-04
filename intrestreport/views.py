from django.shortcuts import render
from buildings.models import Building

# Create your views here.
def main(request):
    cities = Building.get_city_list()
    if request.method == "PUT":
        return render(request, "intrestreport/bostad.html",{"success":True,"cities":cities})
    return render(request, "intrestreport/bostad.html",{"cities":cities})

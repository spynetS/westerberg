from django.http import HttpResponse
import re
from django.shortcuts import render

from .models import ServiceReport

# Create your views here.

def create_report(request):
   reqs = {}
   empty = False
   for item in request.POST:
      reqs[item] = request.POST[item]
      if request.POST[item] == "":
         empty = True
         print(reqs)
   if empty:
      return render(request, "servicereport/form.html",dict({"error":f"{item.title()} Inte i fyllt. Fyll i alla!"}.items()|reqs.items()))

   reg = re.compile("\d{3}[ ]?\d{2}")
   if not reg.match(request.POST["Postnummer"]):
      return render(request, "servicereport/form.html",dict({"error":f"Postnummer format stämmer inte. 123 45 eller 12345"}.items()|reqs.items()))

   
   try:
      report = ServiceReport(
         name=request.POST['Namn'],
         email=request.POST['Epost'],
         phone=request.POST['Telefonnummer'],
         adress=request.POST['Adress'],
         postnumber=request.POST['Postnummer'],
         area=request.POST['Ort'],
         homedate=request.POST['Hemmadatum'],
         homefrom=request.POST['Hemmafrom'],
         hometo=request.POST['Hemmato'],
         description =request.POST['Felbeskrivning'],
      )
      report.save()
   except Exception as e:
      return render(request, "servicereport/form.html",{"error":e})

   return render(request, "servicereport/form.html",{"sucess":True})

def getform(request):
   return render(request, "servicereport/form.html",{})

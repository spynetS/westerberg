from django.http import HttpResponse
from django.shortcuts import render

from .models import ServiceReport

# Create your views here.

def create_report(request):
   for item in request.POST:
      if request.POST[item] == "":
         return render(request, "servicereport/form.html",{"error":f"{item.title()} Inte i fyllt. Fyll i alla!"})

   try:
      report = ServiceReport(
         name=request.POST['Namn'],
         email=request.POST['E-post'],
         phone=request.POST['Telefonnummer'],
         adress=request.POST['Adress'],
         postnumber=request.POST['Postnummer'],
         area=request.POST['Ort'],
         homedate=request.POST['Hemmadatum'],
         homefrom=request.POST['Hemma fr.o.m. kl'],
         hometo=request.POST['Hemma t.o.m. kl'],
         description =request.POST['Felbeskrivning'],
      )
      report.save()
   except Exception as e:
      return render(request, "servicereport/form.html",{"error":e})

   return render(request, "servicereport/form.html",{"sucess":True})

def getform(request):
   return render(request, "servicereport/form.html",{})

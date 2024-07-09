
from django.http import HttpResponse
import re
from django.shortcuts import render
from westerberg import settings

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
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

   reg = re.compile("\\d{3}[ ]?\\d{2}")
   if not reg.match(request.POST["Postnummer"]):
      return render(request, "servicereport/form.html",dict({"error":f"Postnummer format stämmer inte. 123 45 eller 12345"}.items()|reqs.items()))

   post = request.POST["Postnummer"]
   if " " in post:
      post = post.replace(" ","")

   try:
      report = ServiceReport(
         name=request.POST['Namn'],
         email=request.POST['Epost'],
         phone=request.POST['Telefonnummer'],
         adress=request.POST['Adress'],
         postnumber=post,
         area=request.POST['Ort'],
         homedate=request.POST['Hemmadatum'],
         homefrom=request.POST['Hemmafrom'],
         hometo=request.POST['Hemmato'],
         description =request.POST['Felbeskrivning'],
      )
      report.save()

      data = request.POST.copy()

      if "Huvudnyckel" in data:
         data["Huvudnyckel"] = "Ja" if data["Huvudnyckel"] == "on" else "Nej"
      else :
         data["Huvudnyckel"] = "Nej"

      body = render_to_string("servicereport/email.html",context=data,request=request)

      email = EmailMessage(
         f'Serviceanmälan {data["Ort"]}',
         body,
         settings.EMAIL_HOST_USER,
         ['alfred@stensatter.se'],
      )
      email.content_subtype = "html"  # Ensure the email content type is set to HTML
      email.send()



   except Exception as e:
      return render(request, "servicereport/form.html",{"error":e})

   return render(request, "servicereport/form.html",{"sucess":True})

def getform(request):
   return render(request, "servicereport/form.html",{})

import time
from django.http import HttpResponse
from django.shortcuts import render

from .models import News

# Create your views here.
def create_news(request):
    req = request.POST
    if req["title"] == "" or req["description"] == "":
        news = News.objects.all()
        return render(request,'news/form.html',{'news':news,"msg":"Du måste fylla i titel och beskrivning"})

    news = News(title=req['title'],description=req['description'],image=request.FILES['image'])
    news.save()
    news = News.objects.all()
    return render(request,'news/form.html',{'news':news,"msg":"Nyheten har lagts till"})

def page(request):
    news = News.objects.all()
    return render(request,'news/form.html',{'news':news})

def cards(request):
    news = News.objects.all()[:3]
    return render(request,'news/card.html',{'news':news})

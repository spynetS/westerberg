import time
from django.http import HttpResponse
from django.shortcuts import render

from .models import News

# Create your views here.
def create_news(request):
    req = request.POST
    if req["title"] == "" or req["description"] == "":
        news = News.objects.all()
        return render(request,"components/Alert.html",{"type":"error", "msg":"Du måste fylla i alla fält"})

    if 'image' in request.FILES:
        news = News(title=req['title'],description=req['description'],image=request.FILES['image'])
    else:
        news = News(title=req['title'],description=req['description'])
    news.save()
    news = News.objects.all()
    return render(request,"components/Alert.html",{"type":"success", "msg":"Nyheten har laggt tills"})

def edit(request):
    if request.user.is_superuser:
        return render(request,"components/Alert.html",{"type":"success", "msg":"Nyheten har ändrats"})
    return render(request,"components/Alert.html",{"type":"Error", "msg":"You are not admin"})


def delete(request):
    if request.user.is_superuser:
        news = News.objects.get(pk=request.POST["pk"])
        news.delete()
        return render(request,"components/Alert.html",{"type":"success", "msg":"Nyheten har tagitsbort"})
    return render(request,"components/Alert.html",{"type":"Error", "msg":"You are not admin"})

def page(request):
    news = News.objects.all()
    return render(request,'news/form.html',{'news':news})

def cards(request):
    news = News.objects.all()[:3]
    return render(request,'news/card.html',{'news':news})

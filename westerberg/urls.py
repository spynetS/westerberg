"""
URL configuration for westerberg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin as adm
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from buildings.views import fast
from buildings.models import Building
from accounts.models import CustomUser
from westerberg.mail import sendmail
from rentals.views import ledigt, ledigt_lokaler


from rentals.models import Rental
from news.models import News
from westerberg import settings

from django.core.mail import EmailMessage
from django.shortcuts import render

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = [
            ['/static/slides/2.png','Åby. Resturangtorg. Gamla blomaffären blev Resturang fond. Anpassningar för bättre miljö och tillgänglighetet'],
            ['/static/slides/3.png','Söderköping. Från Creperi till bryggeri. Söderköping gick återigen ett bryggeri. Lock, Hop & Barrel flyttade in i tidigare Bondens loaler. Anpassningen och ombygnaden för ett microbryggeri ingick i det nya konceptet.'],
            ['/static/slides/4.png','Söderköping. Banklokalen vid Hagatorget blev ett nytt nav för nya affärer och nätverkande. Näringhslivet och kommuninvånarna i Söderköping erhäll en ny mötesplatsm, CoOperate Coffice. Loalerna anpassades med teknik, visningsytor mötesrum samt kontorsytor för längre eller kortare tids hyra.'],
            ['/static/slides/5.png','Var vill du etablera dig i framtiden?'],
            ['/static/slides/6.png','I söderköping har vi lokaler från 100 till 600 kvm som kan anpassas och förändras för din verksamhet. Samtliga belägna i gatuplan med bra kommunikation och centrumläge'],
            ['/static/slides/7.png','I åby har vi mindre kontros och versamhetslokaler från 60 till 100kvm. Dessutom finns en större 600kvm butikslokal. Samtliga belägna i Åby Centrum med god tillgång till parkeringsplatser']
                            ]

        amount_of_news = 7
        news = News.objects.order_by('-created_at')[:amount_of_news]
        context['news'] = news
        return context

class NewsView(TemplateView):
    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = reversed(News.objects.all())
        return context

class BuildingView(TemplateView):
    template_name = "byggnad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buildings'] = Building.objects.all()
        context['areas'] = Building.get_area_list()
        context['cities'] = Building.get_city_list()
        return context

class RentalView(TemplateView):
    template_name = "byggnad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rentals'] = Rental.objects.filter(lokal=False)
        context['buildings'] = [(building.pk, building.adress) for building in Building.objects.all()]
        return context

class LokalerView(TemplateView):
    template_name = "byggnad.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rentals'] = Rental.objects.filter(lokal=True)
        context['buildings'] = [(building.pk, building.adress) for building in Building.objects.all()]
        context['types'] = Rental.get_lokaltype_list()
        return context

class KontaktView(TemplateView):
    template_name = "kontakt.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def kontakt(request):
    try:
        body = (
            f"Namn: {request.POST['name']}\n"
            f"E-post: {request.POST['email']}\n"
            f"Telefonnummer: {request.POST['phone']}\n"
            f"Meddelande:\n {request.POST['msg']}"
        )


        sendmail(request.POST["subject"],body,request.POST['name'],request.POST['email'],settings.INFO_EMAIL,"Inforeport")

        return render(request,"components/Alert.html",{"type":"success","msg":"Meddelandet skickat!"})
    except:
        return render(request,"components/Alert.html",{"type":"error","msg":"Något gick fel!"})

urlpatterns = [
    path("", HomeView.as_view(template_name="home.html"), name="home"),
    path("admin/", TemplateView.as_view(template_name="admin/admin.html"), name="admin"),
    path("admin/nyheter", NewsView.as_view(template_name="admin/news.html"), name="admin"),
    path("admin/byggnader", BuildingView.as_view(template_name="admin/byggnader.html"), name="admin"),
    path("admin/legenheter", RentalView.as_view(template_name="admin/rental.html"), name="admin"),
    path("admin/lokaler", LokalerView.as_view(template_name="admin/lokaler.html"), name="admin"),

    path('superadmin/', adm.site.urls),
    path("fastigheter/", fast, name="fastigheter"),
    path("lediga-lagenheter", ledigt, name="fastigheter"),
    path("lediga-lokaler", ledigt_lokaler, name="fastigheter"),
    path("nyheter/", NewsView.as_view(template_name="news.html"), name="fastigheter"),
    path("serviceanmalan/", TemplateView.as_view(template_name="serviceanmalan.html"), name="fastigheter"),
    path("intresseanmalan/", TemplateView.as_view(template_name="intressreport.html"), name="fastigheter"),
    path("intresseanmalan/bostad", TemplateView.as_view(template_name="bostad.html"), name="fastigheter"), #
    path("intresseanmalan/lokal", TemplateView.as_view(template_name="lokal.html"), name="fastigheter"), #
    path("hyresgastinformation", TemplateView.as_view(template_name="aboutus.html"), name="fastigheter"),
    path("kontakt",KontaktView.as_view(template_name="kontakt.html")),
    path("kontakt/skicka/",kontakt),


    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("buildings/", include("buildings.urls")),
    path("news/", include("news.urls")),
    path("rentals/", include("rentals.urls")),
    path("servicereport/", include("servicereport.urls")),
    path("intrestreport/", include("intrestreport.urls")),
    re_path(r'^sitemap\.xml$', RedirectView.as_view(url='/static/sitemap.xml', permanent=True)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

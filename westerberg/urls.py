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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from buildings.views import fast
from buildings.models import Building
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
        context['images'] = ['/media/slides/2.png', '/media/slides/3.png', '/media/slides/4.png','/media/slides/5.png','/media/slides/6.png','/media/slides/7.png']  # Add your images here
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

def kontakt(request):
    try:
        body = (
            f"Namn: {request.POST['name']}\n"
            f"E-post: {request.POST['email']}\n"
            f"Telefonnummer: {request.POST['phone']}\n"
            f"Meddelande:\n {request.POST['msg']}"
        )

        # Create the email
        email = EmailMessage(
            subject=f"Info {request.POST['subject']}",
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.INFO_EMAIL],
            headers={'Reply-To': request.POST['email']} # add to other emails to??
        )

        # Send the email
        email.send()
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
    path("ledigt/", ledigt, name="fastigheter"),
    path("ledigt/lokaler", ledigt_lokaler, name="fastigheter"),
    path("nyheter/", NewsView.as_view(template_name="news.html"), name="fastigheter"),
    path("serviceanmalan/", TemplateView.as_view(template_name="serviceanmalan.html"), name="fastigheter"),
    path("intresseanmalan/", TemplateView.as_view(template_name="intressreport.html"), name="fastigheter"),
    path("intresseanmalan/bostad", TemplateView.as_view(template_name="bostad.html"), name="fastigheter"), #
    path("intresseanmalan/lokal", TemplateView.as_view(template_name="lokal.html"), name="fastigheter"), #
    path("hyresgastinformation", TemplateView.as_view(template_name="aboutus.html"), name="fastigheter"),
    path("kontakt",TemplateView.as_view(template_name="kontakt.html")),
    path("kontakt/skicka/",kontakt),


    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("buildings/", include("buildings.urls")),
    path("news/", include("news.urls")),
    path("rentals/", include("rentals.urls")),
    path("servicereport/", include("servicereport.urls")),
    path("intrestreport/", include("intrestreport.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)

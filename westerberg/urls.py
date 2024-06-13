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

from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("admin/", TemplateView.as_view(template_name="admin/admin.html"), name="admin"),
    path('superadmin/', adm.site.urls),
    path("fastigheter/", fast, name="fastigheter"),
    path("serviceanmalan/", TemplateView.as_view(template_name="serviceanmalan.html"), name="fastigheter"),

    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("buildings/", include("buildings.urls")),
    path("news/", include("news.urls")),
    path("rentals/", include("rentals.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

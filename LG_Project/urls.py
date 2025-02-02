"""LG_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_pydenticon.views import image as pydenticon_image


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mainapp.url")),
    path("identicon/image/<path:data>", pydenticon_image, name="pydenticon_image"),
    path("upload/", include("uploadapp.urls")),
    path("labeling/", include("labelingapp.url")),
    path("dashboard/", include("dashboard.urls.dashboard")),
    path("output/", include("outputapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

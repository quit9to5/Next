"""patient_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doctor/', 'doctor.views.home', name='home'),
    url(r'^contact', 'doctor.views.contact', name='contact'),
    url(r'^search', 'doctor.views.search', name='search'),
    url(r'^about', 'doctor.views.about', name='about'),
    url(r'^login', 'doctor.views.login', name='login'),
    url(r'^doctor_logout', 'doctor.views.doctor_logout', name='logout'),
    url(r'^doctor_loggedin', 'doctor.views.doctor_loggedin', name='doctor_login'),
    url(r'^doctor_login', 'doctor.views.doctor_login', name='doctor_login'),
    url(r'^auth/', 'doctor.views.doctor_auth', name='doctor_auth'),
    url(r'^', 'doctor.views.home', name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

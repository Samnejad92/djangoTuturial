"""
URL configuration for DjangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from djan.views import index, about_us, contact_us, login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact-us', contact_us),
    path('about-us', about_us),
    path('login', login_page),
    path('register', register_page),
]

urlpatterns = urlpatterns + static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
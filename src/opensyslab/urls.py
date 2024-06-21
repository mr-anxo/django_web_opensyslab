"""
URL configuration for opensyslab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from opensyslab.views import home, about, portfolio_item, portfolio_overview, pricing, contact, faq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about', about, name="about"),
    path('pricing', pricing, name="pricing"),
    path('contact', contact, name="contact"),
    path('faq', faq, name="faq"),
    path('portfolio', portfolio_overview, name="portfolio"),
    path('portfolio_details', portfolio_item, name="portfolio_details"),
    path('blog/', include("blog.urls")),
]

"""critterretail URL Configuration

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
from . import views
from . import apis

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'product/(?P<productID>[0-9]+)$', views.product),

    url(r'api/products', apis.products),
    url(r'api/product/(?P<productID>[0-9]+)/review', apis.addProductReview),
    url(r'api/confirmPayment/(?P<code>[0-9]+)', apis.confirmPayment),
    url(r'api/completePurchase', apis.completePurchase),
]

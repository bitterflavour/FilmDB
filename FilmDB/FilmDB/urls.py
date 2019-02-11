from django.conf.urls import url, include
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^movie/', include('movie.urls')),
    url(r'^$', views.index, name='index'),
    url(r'.*', lambda request: render(request, '404.html'), name='404'),
]

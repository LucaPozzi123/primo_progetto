
#from django.contrib import admin
from django.urls import path
from .views import index3,somma,media
app_name="prova_pratica_0"
urlpatterns = [
    path('',index3,name='index3'),
    path('somma',somma,name='somma'),
    path('media',media,name='media')
]

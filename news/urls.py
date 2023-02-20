from django.urls import path
from .views import home, ArticoloDetailViewCB, ArticoloListView, giornalista_api, giornalisti_list_api, articoli_api, articoli_list_api

app_name = 'news'

urlpatterns = [
    path('',home,name="homeview"),
    path("articoli/<int:pk>", ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path("lista_articoli/",ArticoloListView.as_view(),name="lista_articoli"),
    path("giornalista_api/<int:pk>",giornalista_api,name="giornalista_api"),
    path("giornalisti_list_api/",giornalisti_list_api,name="giornalisti_lista_api"),
    path("articoli_api/<int:pk>",articoli_api,name="articoli_api"),
     path("articoli_list_api/",articoli_list_api,name="articoli_list_api"),
]
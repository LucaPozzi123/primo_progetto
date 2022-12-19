from django.urls import path
from .views import view_a, view_b,menu

app_name="prova_pratica_2"

urlpatterns=[
    path('',menu,name='menu'),
    path('view_a',view_a,name='view_a'),
    path('view_b',view_b,name='view_b'),
   
]

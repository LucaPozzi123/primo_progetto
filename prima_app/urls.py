from django.urls import path
from .views import homepage,welcome,lista,variabili,index,chi_siamo
app_name="prima_app"
urlpatterns=[
    path('',homepage,name='homepage'),
    path('welcome',welcome,name='welcome'),
    path('lista',lista,name='lista'),
     path('chi_siamo',chi_siamo,name='chi_siamo'),
    path('variabili',variabili,name='variabili'),
    path('index',index,name='index')
   


]
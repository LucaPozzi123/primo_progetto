from django.http import HttpResponse
from .models import Articoli,Giornalista
from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse
# Create your views here.
def home(request):
    articoli = Articoli.objects.all()
    giornalisti= Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage_news.html", context)

def articoloDetailView(request, pk):
    articolo = get_object_or_404(Articoli, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB(DetailView):
    model = Articoli
    template_name = "articolo_detail.html"

class ArticoloListView(ListView):
    model=Articoli
    template_name="lista_articoli.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["articoli"]=Articoli.objects.all()
        return context

def giornalisti_list_api(request):
    giornalisti=Giornalista.objects.all()
    data={'giornalisti':list(giornalisti.values("pk","nome","cognome"))}
    response=JsonResponse(data)
    return response

def giornalista_api(request,pk):
    try:
        giornalista=Giornalista.objects.get(pk=pk)
        data={'giornalista':{
            "nome":giornalista.nome,
            "cognome":giornalista.cognome,
            }
        }
        response=JsonResponse(data)
    except Giornalista.DoesNotExist:
        response=JsonResponse({
        "error":{
            "code":404,
            "message":"Giornalista non trovato"
        }},
        status=404)
    return response

def articoli_list_api(request):
    articoli=Articoli.objects.all()
    data={'articoli':list(articoli.values("pk","titolo","contenuto"))}
    response=JsonResponse(data)
    return response

def articoli_api(request,pk):
    try:
        articoli=Articoli.objects.get(pk=pk)
        data={'articolo':{
            "titolo":articoli.titolo,
            "contenuto":articoli.contenuto,
            }
        }
        response=JsonResponse(data)
    except Articoli.DoesNotExist:
        response=JsonResponse({
        "error":{
            "code":404,
            "message":"Articolo non trovato"
        }},
        status=404)
    return response

class GiornalistaDetailViewCB(DetailView):
    model=Giornalista
    template_name="giornalista_detail.html"

class GiornalistaListView(ListView):
    model=Giornalista
    template_name="lista_giornalisti.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['giornalisti']=Giornalista.objects.all()
        return context

def tabellaG(request):
    return render(request,"tabellaG.html")

def tabellaA(request):
    return render(request,"tabellaA.html")

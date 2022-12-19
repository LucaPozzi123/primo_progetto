from django.http import HttpResponse
from .models import Articoli,Giornalista
from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
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



from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def welcome(request):
    return render(request,"welcome.html")

def lista(request):
    return render(request,"lista.html")

def chi_siamo(request):
    return render(request,"chi_siamo.html")

def variabili(request):
    context={
        'var1':'Prima varibile',
        'var2':'Seconda varibile',
        'var3':'Terza varibile',
    }
    return render(request,"variabili.html",context)

def index(request):
    return render(request,"index.html")


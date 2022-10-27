from django.shortcuts import render 
import random

# Create your views here.
def index3(request):
    return render(request,"index3.html")

def somma(request):
    x=random.randint(1,10)
    y=random.randint(1,10)
    s=x+y
    context={
       'x':x,
       'y':y,
       's':s,
    }
    return render(request,"somma.html",context)

def media(request):
    lista=[]
    for i in range(30):
        lista.append(random.randint(1,10))
    context={
        'lista':lista,
        'media':sum(lista)/30,
    }
    return render(request,"media.html",context)


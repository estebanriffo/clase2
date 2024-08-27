from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>soy el index de la app2 </h1>")

def queso(request):
    html="""
    <h1 style="color:yellow">
    cheese
    </h1>    
    """
    return HttpResponse(html)

def chistemalo(request):
    html="""
    <h2>como queda un mago despues del almuerzo???</h2>
    <h1>MAGORDITO</h1>
    <a href="/app2/index">volver</a>
    """
    return HttpResponse(html)
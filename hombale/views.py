from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def kgf(request):
    return HttpResponse("<h1><center>KGF is an Action Movie<center></h1> <h2><center>Rocky, a young man, seeks power"
                        "and wealth in order to fulfil a promise to his dying mother. His quest takes him to Mumbai,"
                          "where he gets involved with the notorious gold mafia<center></h2>")

def slaar(request):
    return HttpResponse("<h1><center>SALAAR is an Action Movie<center></h1> <h2><center>A gang leader makes a promise"
                         "to a dying friend by taking on other criminal gangs.<center></h2>")
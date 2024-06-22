from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tumbbad(request):
    return HttpResponse("<h1><center>TUMBBAD is Horror Movie<center></h1> <h2><center>When a family builds a shrine for Hastar,"
                        "a monster who is never to be worshipped, and attempts to get their hands on his cursed wealth,"
                          "they face catastrophic consequences.<center></h2>")

def partner(request):
    return HttpResponse("<h1><center>PARTNER is Comedy Movie<center></h1> <h2><center>Prem, a love guru who shares tips on dating women,"
                         "helps his client, Bhaskar, woo his boss. However, he later falls for a single mother and"
                           "tries to hide his profession.<center></h2>")
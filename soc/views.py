from django.shortcuts import render, HttpResponse
from . models import *
import datetime

def vypis_skola(request):
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "soc/index.html", {"studenti": studenti, "ucitelia": ucitelia})


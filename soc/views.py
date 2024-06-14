from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from . models import *
import datetime
from .forms import TemaForm

def vypis_skola(request):
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    odbory = Odbor.objects.all()
    temy = Tema.objects.all()

    volne_temy = Tema.objects.filter(dostupnost='Voľne')
    cakajuce_temy = Tema.objects.filter(dostupnost='Čakajúce')
    obsadene_temy = Tema.objects.filter(dostupnost='Obsadené')

    temy = list(volne_temy) + list(cakajuce_temy) + list(obsadene_temy)

    return render(request, "soc/index.html", {
        "studenti": studenti,
        "ucitelia": ucitelia,
        "tema": temy,
        "odbor": odbory
    })

def nova_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soc') 
    else:
        form = TemaForm()
    return render(request, 'soc/tema.html', {'form': form})

def konzultant_detail(request, konzultant_id):
    tema = Tema.objects.filter(konzultant_id=konzultant_id)
    return render(request, 'soc/konzultant_detail.html', {"tema": tema})

def student_detail(request, student_id):
    tema = Tema.objects.filter(student_id=student_id)
    return render(request, 'soc/student_detail.html', {"tema": tema})

def update_konzultacie(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    if request.method == 'POST':
        
        tema.konzultacie = request.POST.get('konzultacie')
        tema.save()
        return redirect('soc')  
    return render(request, 'update_konzultacie.html', {'tema': tema})


def statistiky(request):
    pocet_tema = Tema.objects.count()
    pocet_volnych_tem = Tema.objects.filter(dostupnost='Voľne').count()
    pocet_obsadenych_tem = Tema.objects.filter(dostupnost='Obsadené').count()
    pocet_cakajucich_tem = Tema.objects.filter(dostupnost='Čakajúce').count()
    pocet_studentov = Student.objects.count()
    pocet_ucitelov = Ucitel.objects.count()

    context = {
        'temy': pocet_tema,
        'volne': pocet_volnych_tem,
        'obsadene': pocet_obsadenych_tem,
        'cakajuce': pocet_cakajucich_tem,
        'studenti': pocet_studentov,
        'ucitelia': pocet_ucitelov,
    }
    return render(request, 'soc/statistiky.html', context)
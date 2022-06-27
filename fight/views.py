from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from fight.forms import CreateGato
from fight.models import Gatos
from fight.forms import eliminar
from .fight import fight2

# Create your views here.

def home(response):
    return render(response, 'fight/base.html', {})

def list(response, id):
    forms=eliminar()
    if response.method == "POST":
        forms = eliminar(response.POST)
        if forms.is_valid():
            check=forms.cleaned_data['eliminar']
            if check == True:
                f=Gatos.objects.get(id=id)
                f.delete()
                return HttpResponseRedirect('../baseDatos')
    gatos = Gatos.objects.get(id=id)
    return render(response, 'fight/list.html', {'gato':gatos, 'forms':forms, 'id':id})

def datos(response):
    gatos = Gatos.objects.all()
    return render (response, 'fight/datos.html', {'gatos':gatos})
    

def create(response):
    
    if response.method == "POST":
        forms = CreateGato(response.POST)
        
        if forms.is_valid():
            nomb = forms.cleaned_data["name"]
            est = forms.cleaned_data["estilo"]
            descr= forms.cleaned_data["descr"]
            print(est[0])
            if est[0] == "Bonito":
                Ps = 30
                Pcrit = 0.1
                Ev = 1.2
                At = 8
            elif est[0] == "Astuto":
                Ps = 20
                Pcrit = 0.35
                Ev = 2
                At = 5
            elif est[0] == "Peligroso":
                Ps = 25
                Pcrit = 0.25
                Ev = 1.5
                At = 10
                
            t = Gatos(Nombre=nomb,EstiloCombate=est[0],Descripcion=descr,PuntosVida=Ps,ProbabilidadCritico=Pcrit,Evasion=Ev,Ataque=At)
            t.save()
            
        return HttpResponseRedirect('../%i' %t.id)
            
    else:
        forms = CreateGato()
    return render(response, "fight/create.html", {"form":forms})

def fight(response):
    x=fight2(5,6)
    return render(response, 'fight/fight.html', {'x':x})
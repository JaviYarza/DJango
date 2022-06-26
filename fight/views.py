from django.http import HttpResponse
from django.shortcuts import render

from fight.forms import CreateGato
from fight.models import Gatos

# Create your views here.

def home(response):
    return render(response, 'fight/base.html', {})

def list(response, id):
    gatos = Gatos.objects.get(id=id)
    return render(response, 'fight/list.html', {'gato':gatos})
    

def create(response):
    
    if response.method == "POST":
        forms = CreateGato(response.POST)
        
        print("Estoy aqui")
        
        if forms.is_valid():
            print("Ahora aqui")
            nomb = forms.cleaned_data["name"]
            est = forms.cleaned_data["estilo"]
            descr= forms.cleaned_data["descr"]
            print(est[0])
            if est[0] == "Bonito":
                Ps = 30
                Pcrit = 0.3
                Ev = 3
                At = 7
            elif est[0] == "Astuto":
                Ps = 20
                Pcrit = 0.7
                Ev = 5
                At = 8
            elif est[0] == "Peligroso":
                Ps = 25
                Pcrit = 0.5
                Ev = 2
                At = 10
            print(nomb, est, descr, Ps, Pcrit, Ev, At)
                
            t = Gatos(Nombre=nomb,EstiloCombate=est[0],Descripcion=descr,PuntosVida=Ps,ProbabilidadCritico=Pcrit,Evasion=Ev,Ataque=At)
            t.save()
            
        return HttpResponse("Se ha creado el gatito correctamente")
            
    else:
        forms = CreateGato()
    return render(response, "fight/create.html", {"form":forms})
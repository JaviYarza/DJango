from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .form import BuscaLista, CreateNewList
'''
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1> %s </h1> <br></br> <p>%s</p>" %(ls.name, str(items.text)))
'''

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            check = form.cleaned_data["check"]
            a= form.cleaned_data["text"]
            t = ToDoList(name=n)
            t.save()
            t.item_set.create(text=a, complete=check)
            
        return HttpResponseRedirect("/main/%i" %t.id)
            
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def delete(response):
    if response.method == "POST":
        form = BuscaLista(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList.objects.get(name=n)
            t.delete()
            
        return HttpResponse("Se ha eliminado correctamente el elemento")
            
    else:
        form = BuscaLista()
    return render(response, "main/delete.html", {"form":form})



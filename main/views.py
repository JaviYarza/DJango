from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreateNewList
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
            t = ToDoList(name=n)
            t.save()
            
        return HttpResponseRedirect("/%i" %t.id)
            
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})



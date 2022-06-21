from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
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



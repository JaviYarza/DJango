from django.urls import path

from . import views

urlpatterns = [
    path("", views.home , name="home" ),
    path("create/", views.create, name="crear"),
    path("<int:id>/", views.list, name="listar"),
    path("baseDatos/", views.datos, name="datos"),
    path("fight/", views.fight, name="lucha"),
]
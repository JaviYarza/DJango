from django.db import models

class Gatos(models.Model):
    Nombre= models.CharField(max_length=200, unique=True)
    EstiloCombate= models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)
    PuntosVida = models.DecimalField(default= 20, max_digits=4,decimal_places=2)
    ProbabilidadCritico = models.DecimalField(default = 0,max_digits=4,decimal_places=2)
    Evasion = models.DecimalField(default = 0,max_digits=4,decimal_places=2)
    Ataque = models.DecimalField(default=10, max_digits=4,decimal_places=2)
    
    def __str__(self):
        return self.Nombre
    
class Perros(models.Model):
    Nombre= models.CharField(max_length=200, unique=True)
    EstiloCombate= models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)
    PuntosVida = models.DecimalField(default= 20, max_digits=4,decimal_places=2)
    ProbabilidadCritico = models.DecimalField(default = 0,max_digits=4,decimal_places=2)
    Evasion = models.DecimalField(default = 0,max_digits=4,decimal_places=2)
    Ataque = models.DecimalField(default=10, max_digits=4,decimal_places=2)
    
    def __str__(self):
        return self.Nombre
    
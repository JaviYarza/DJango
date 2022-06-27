from fight.models import Gatos
import numpy as np

def fight2(id1, id2):
    gato1 = Gatos.objects.get(id=id1)
    gato2 = Gatos.objects.get(id=id2)
    vida1= gato1.PuntosVida
    vida2= gato2.PuntosVida
    print("En la esquina de la izquierdaaaaa tenemos a: "+ gato1.Nombre , gato1.Descripcion)
    print("Y como su contrincante tenemos a: "+ gato2.Nombre , gato2.Descripcion)
    print("QUE EMPIECEN LAS TORTAS")
    while (vida1>0 | vida2>0):
        ev1=(1/gato1.Evasion)
        ev2=(1/gato2.Evasion)
        x1=np.random.randn()
        x2=np.random.randn()
        if x1 < ev2:
            print(gato1.Nombre + 'ha fallado estreipotosamente su ataque')
        else:
            if x1 > (1-gato1.ProbabilidadCritico):
                ataque1=(gato1.Ataque)*2
            else:
                ataque1= gato1.Ataque
            vida2=vida2-ataque1
            print(gato2.Nombre +" ha sido atacado ferozmente y ha perdido:" + str(ataque1) + "puntos de vida")
            print(vida2)
        if x2 < ev1:
            print(gato2.Nombre + ' ha fallado estreipotosamente su ataque')
        else:
            if x2 > (1-gato2.ProbabilidadCritico):
                ataque2=(gato2.Ataque)*2
            else:
                ataque2= gato2.Ataque
            vida1=(vida1-ataque2)
            print(gato1.Nombre +" ha sido atacado ferozmente y ha perdido:" + str(ataque2) + "puntos de vida")
            print(vida1)
    
    print("La batalla ha acabado...")
    if (vida1<0 and vida2<0):
        print(gato1.Nombre + " y " + gato2.Nombre + " se han matado mutuamente... \n No hay supervivientes!")
    if (vida2>0):
        print("El vencedor es: "+ gato2.Nombre)
    if (vida1>0):
        print("El vencedor es: "+ gato1.Nombre)

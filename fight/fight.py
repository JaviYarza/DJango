from fight.models import Gatos
import numpy as np

def fight2(id1, id2):
    gato1 = Gatos.objects.get(id=id1)
    gato2 = Gatos.objects.get(id=id2)
    vida1= gato1.PuntosVida
    vida2= gato2.PuntosVida
    x="En la esquina de la izquierdaaaaa tenemos a: "+ str(gato1.Nombre)
    x += str(gato1.Descripcion)
    x += "\n Y como su contrincante tenemos a: "+ str(gato2.Nombre)
    x += str(gato2.Descripcion)
    while (vida1>0 and vida2>0):
        ev1=(1/gato1.Evasion)
        ev2=(1/gato2.Evasion)
        x1=np.random.rand()
        x2=np.random.rand()
        if x1 < ev2:
            x += "\n"+ gato1.Nombre + " ha fallado estreipotosamente su ataque"
        else:
            if x1 > (1-gato1.ProbabilidadCritico):
                ataque1=(gato1.Ataque)*2
                x+="\n CRITICO de " + str(gato1.Nombre)
            else:
                ataque1= gato1.Ataque
            vida2=vida2-ataque1
            x+="\n"+ str(gato2.Nombre) +" ha sido atacado ferozmente y ha perdido:" + str(ataque1) + "puntos de vida"
        if x2 < ev1:
            x+="\n"+ str(gato2.Nombre) + " ha fallado estreipotosamente su ataque"
        else:
            if x2 > (1-gato2.ProbabilidadCritico):
                ataque2=(gato2.Ataque)*2
                x+="\n CRITICO de " + str(gato2.Nombre)
            else:
                ataque2= gato2.Ataque
            vida1=(vida1-ataque2)
            x+="\n" + str(gato1.Nombre) + " ha sido atacado ferozmente y ha perdido:" + str(ataque2) + "puntos de vida"
    
    x +="\n La batalla ha acabado..."
    if (vida1<0 and vida2<0):
        x +="\n" + str(gato1.Nombre) + " y " + str(gato2.Nombre) + " se han matado mutuamente... \n No hay supervivientes!"
    if (vida2>0):
        x +="\n El vencedor es: " + str(gato2.Nombre)
    if (vida1>0):
        x +="\n El vencedor es: " + str(gato1.Nombre)
    return x
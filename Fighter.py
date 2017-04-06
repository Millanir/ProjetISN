from tkinter import*
from random import randint

    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)

health =healthMax
healthStr ="/"+str(healthMax)


def jeudes () :
    var = randint (1,100) #une variable aléat entre 1 et 100
    resu = 0 #pour initiliser variable qu'on retournera +tard
    if var>90 :
        resu=4 #valeur a retourner
    elif var>50 :
        resu=3
    elif var>10 :
        resu=2
    else :
        resu=1
    return resu #valeur retourné utilisable

def attaque():
    global healthE
    test=jeudes
    if test == 1:
        health=health-3
        healthE=healthE
        return health,healthE
    elif test==2:
        healthE=healthE
        health=health
        return healthE,health
    elif test==3:
        healthE=healthE-3
        health=health
        return healthE,health
    elif test==4:
        healthE=healthE-6
        health=health




def defense():
    global healthE
    global health
    counter=randint(1,100)
    if counter>90:
        healthE=healthE-7
    elif counter>75:
        healthE=healthE-2
    elif counter>50:
        healthE=healthE
    elif counter>10:
        health=health-2
    else:
        health=health-5
def fighter(lvl):
    global healthE
    healthE=lvl*10
    healthEM=healthE
    healthEstr="/"+str(healthEM)
    ff=Tk()
    ff.title("Combat en cours")
    ff.geometry ("500x500")
    canS= Frame(ff,bg="white",height=250,width=500)
    canS.pack()
    sf=Frame(ff,height=250,width=500)
    sf.pack(side=BOTTOM)
    f2=Frame(sf,height=250,width=250)
    f2.pack(side=LEFT,padx=100,pady=100)
    bou1=Button(f2,text='Attaquer',command=attaque)
    bou1.pack()
    bou1.grid(row=0,column=0)
    bou2=Button(f2,text='Defendre',command=defense)
    bou2.pack()
    bou2.grid(row=1,column=0)
    f3=Frame(sf,height=250,width=250)
    f3.pack(side=RIGHT)
    f31=Frame(f3)
    f31.grid(row=0)
    pv=Message(f31,text="PV=")
    pv.grid(row=0,column=0)
    pv1=Message(f31,text=health)
    pv1.grid(row=0,column=1)
    pv2=Message(f31,text=healthStr)
    pv2.grid(row=0,column=2)
    n=Message(f31,text="   ")
    n.grid(row=1)
    ste=Message(f3,text="Stat ennemi")
    ste.grid (row=1,column=0)
    pva=Message(f3,text="PV=")
    pva.grid(row=2,column=0)
    pva1=Message(f3,text=healthE)
    pva1.grid(row=2,column=1)
    pva2=Message(f3,text=healthEstr)
    pva2.grid(row=2,column=3)
    if healthE<1:
        ff.destroy
        return 1
    elif health<1:
        ff.destroy
        return 0
    ff.mainloop()




fighter(1)

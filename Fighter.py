from tkinter import*
from random import randint

    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)

health =healthMax
healthStr ="/"+str(healthMax)


def jeudes():
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













def fighter(lvl):
    global healthE,health
    healthE=lvl*10
    healthEM=healthE
    healthEstr="/"+str(healthEM)

    def changeStats():
        tableau.delete('all')

        tableau.create_text(50, 100, text="Stats Ennemi")
        tableau.create_text(50, 50, text="Vos stats")

        tableau.create_text(50,65, text= "PV=  {} / {} ".format(health,healthMax))
        tableau.create_text(50,115,text= "PV=  {} / {} ".format(healthE,healthEM))


    def attaque():
        global healthE,health
        test=jeudes()
        if test == 1:
            health=health-3
        elif test==3:
            healthE=healthE-3
        elif test==4:
            healthE=healthE-6
        changeStats()

    def defense():
        global healthE,health
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
        changeStats()


    ff=Tk()
    ff.title("Combat en cours")
    ff.geometry ("500x500")
    canS= Frame(ff,bg="white",height=250,width=500)
    canS.pack()
    sf=Frame(ff,height=250,width=500)
    sf.pack(side=BOTTOM)
    f2=Frame(sf,height=250,width=250)
    f2.pack(side=LEFT,padx=100,pady=100)

    f3=Frame(sf,height=100,width=200)
    f3.pack(side=RIGHT)
    tableau = Canvas(f3, height= 180, width=200)
    tableau.pack()
    bou1=Button(f2,text='Attaquer',command=attaque)
    bou1.pack()
    bou1.grid(row=0,column=0)
    bou2=Button(f2,text='Defendre',command=defense)
    bou2.pack()
    bou2.grid(row=1,column=0)

    def close():
        ff.after(150, close)
        if healthE<= 0:
            ff.destroy()
        elif health<= 0:
            ff.destroy()
        else:
            pass
    close()

    ff.mainloop()




fighter(1)
=======
﻿from tkinter import*
from random import randint

    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)

health =healthMax
healthStr ="/"+str(healthMax)


def jeudes():
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













def fighter(lvl):
    global healthE,health
    healthE=lvl*10
    healthEM=healthE
    healthEstr="/"+str(healthEM)

    def changeStats():
        tableau.delete('all')

        tableau.create_text(50, 100, text="Stats Ennemi")
        tableau.create_text(50, 50, text="Vos stats")

        tableau.create_text(50,65, text= "PV=  {} / {} ".format(health,healthMax))
        tableau.create_text(50,115,text= "PV=  {} / {} ".format(healthE,healthEM))


    def attaque():
        global healthE,health
        test=jeudes()
        if test == 1:
            health=health-3
        elif test==3:
            healthE=healthE-3
        elif test==4:
            healthE=healthE-6
        changeStats()

    def defense():
        global healthE,health
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
        changeStats()


    ff=Tk()
    ff.title("Combat en cours")
    ff.geometry ("500x500")
    canS= Frame(ff,bg="white",height=250,width=500)
    canS.pack()
    sf=Frame(ff,height=250,width=500)
    sf.pack(side=BOTTOM)
    f2=Frame(sf,height=250,width=250)
    f2.pack(side=LEFT,padx=100,pady=100)

    f3=Frame(sf,height=100,width=200)
    f3.pack(side=RIGHT)
    tableau = Canvas(f3, height= 180, width=200)
    tableau.pack()
    bou1=Button(f2,text='Attaquer',command=attaque)
    bou1.pack()
    bou1.grid(row=0,column=0)
    bou2=Button(f2,text='Defendre',command=defense)
    bou2.pack()
    bou2.grid(row=1,column=0)

    def close():
        ff.after(150, close)
        if healthE<= 0:
            ff.destroy()
        elif health<= 0:
            ff.destroy()
        else:
            pass
    close()

    ff.mainloop()




fighter(1)
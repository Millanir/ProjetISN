from tkinter import*
from random import randint

    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)
pveperdu=0
pvperdu=0
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
    def avancer():
        deroulement.delete('all')
        deroulement.create_text(200,50,text='Point de vie perdu: {}'.format(pvperdu))
        deroulement.create_text(200,100,text="Point de vie perdu par l'ennemi: {}".format(pveperdu))
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
            pvperdu=3
            pveperdu=0
        elif test==3:
            healthE=healthE-3
            pveperdu=3
            pvperdu=0
        elif test==4:
            healthE=healthE-6
            pvperdu=0
            pveperdu=6
        else:
            pveperdu=0
            pveperdu=0
        global pveperdu,pveperdu
        changeStats()
        avancer()

    def defense():
        global healthE,health
        counter=randint(1,100)
        if counter>90:
            healthE=healthE-7
            pveperdu=7
            pvperdu=0
        elif counter>75:
            healthE=healthE-2
            pvperdu=0
            pveperdu=2
        elif counter>50:
            healthE=healthE
            pvperdu=0
            pveperdu=0
        elif counter>10:
            health=health-2
            pveperdu=0
            pvperdu=0
        else:
            health=health-5
            pvperdu=5
            pveperdu=0
        global pvperdu,pveperdu
        avancer()
        changeStats()


    ff=Tk()
    ff.title("Combat en cours")
    ff.geometry ("500x400")
    deroulement=Canvas(ff,height=125,width=500)
    deroulement.pack(side=TOP)
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
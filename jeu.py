#crée par xgbasai & Millanir
from tkinter import*
from random import randint


    #Liste de textes à lire
History=["Story.txt","Right1.txt","Left1.txt"] ##Listes dans des listes?
#Change la liste History en fonction du numéro
number=0

    #numéro de la salle
Sally=0
salle=0
choiSal=[[1,50,13],[2,3,4],[51,52,53]] #Liste de liste pour changer de salle

    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)

health =healthMax
healthStr ="/"+str(healthMax)

    ##Simule un lancement de dès, réusittes/échecs


Objet=[] #Liste de none et de chiffres en fonction si on a ramassé un objet ou pas
item= 0 #Variable qui change en fonction de la salle




for i in range(0,10):
    Objet[i]= Objet.append(i)

def addObj():                   #Ajoute un objet à l'inventaire en fonction de la salle
    Objet[item] =Sally


def Inventory():                #Ouvre la fenêtre Inventaire
    fenInv = Tk()
    fenInv.title("Inventaire")
    fenInv.geometry("350x200")
    framinv = Frame(fenInv)
    def InvObj():
        framinv.destroy()
        if Objet[0] ==1:
            obj1= Message(framinv,text= "Morceau de débris",fg='black',width= "250")
            obj1.pack()
        if Objet[1] ==1:
            obj2= Message(framinv,text= "Lampe torche",width= "250")
            obj2.pack()
    boutan = Button(fenInv,width=8,text="Actualiser",command=InvObj)
    boutan.pack(side=BOTTOM)
    fenInv.mainloop()

def machin():
    global can
    can.destroy()
    can = Frame(fram1, width =350, height =90, bg ='white')
    can.pack(padx =25, pady =20)
    guppy= open(History[number],'r', encoding= 'Utf-8')
    cod = guppy.read()
    guppy.close()
    tex4 = Message(can, text= cod,width=350,bg='white', fg= 'black')
    tex4.pack()



def choix1():
    global number
    number = choiSal[0][salle]
    machin()
    return number

def choix2():
    global number
    number = choiSal[1][salle]
    machin()
    return number

def choix3():
    global number
    number = choiSal[2][salle]
    machin()
    return number

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


    #Fenêtre Tk
    #Fenêtre principale

fen1 = Tk()

fen1.title("Game Project ISN")
fen1.geometry("900x600")

MainFrame = Frame(fen1, bg='dark grey',bd=5, relief=RAISED)
MainFrame.pack(side=LEFT)

fram1= Frame(MainFrame,bg="white", height=350,width=450,bd=6,relief=SUNKEN)
fram1.pack(side=TOP, padx=5)

can = Frame(fram1, width =350, height =90, bg ='white')
can.pack(padx =25, pady =20)

guppy= open("Story.txt",'r', encoding= 'Utf-8')
cod = guppy.read()
tex4 = Message(can, text= cod,width=350,bg='white', fg= 'black')
tex4.pack()
guppy.close()

fram2 = Frame(MainFrame,bg="gray",height=300,width=400)
fram2.pack(side=BOTTOM,padx=25,pady=20)

bou1 = Button(fram2, width=8, text="1",command= choix1)
bou1.pack()
bou1.grid(row= 0,column=0)

bou2=Button(fram2,width=8,text="2",command=choix2)
bou2.pack()
bou2.grid(row=0,column=1)

bou3=Button(fram2,width=8,text='3',command=choix3)
bou3.pack()
bou3.grid(row=0,column=2)

Sframe=Frame(fen1,heigh=350,width=300)
Sframe.pack(side=BOTTOM)

framstat1=Frame(Sframe,height=150,width=200)
framstat1.pack(side=RIGHT,padx=25,pady=20)

texSta0 = Message(framstat1, text= "Pv      =",width=350, fg= 'black')
texSta0.grid(row =0,column=1, sticky =E)

texSta1 = Message(framstat1, text= "Stats :",width=300, fg= 'black')
texSta1.grid(row =1,column=0, sticky =E)

texSta2 = Message(framstat1, text= "Chance  =",width=350, fg= 'black')
texSta2.grid(row =1,column=1, sticky =E)

texSta3 = Message(framstat1, text= "Adresse =",width=350, fg= 'black')
texSta3.grid(row =2,column=1, sticky =E)

texStaPV = Message(framstat1, text= health,width=250, fg= 'red')
texStaPV.grid(row=0,column=2)

texStaChance = Message(framstat1, text= luck,width=250, fg= 'dark green')
texStaChance.grid(row=1,column=2)

texStaAdresse = Message(framstat1, text= finesse,width=250, fg= 'blue')
texStaAdresse.grid(row=2,column=2)

texStaPV = Message(framstat1, text= healthStr,width=250, fg= 'black')
texStaPV.grid(row=0,column=3)

equip=Button(Sframe,width=8,text="Inventaire",command=Inventory)
equip.pack(side=LEFT)

canimg = Canvas(fen1, width =300, height =250, bg ='white')
canimg.pack(side=RIGHT,padx=25,pady=20)
photo = PhotoImage(file ='concept_corpus.gif')
item = canimg.create_image(25, 100, image =photo)













fighter(1)






fen1.mainloop ()
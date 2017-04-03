# Créé par user, le 28/03/2017 en Python 3.2
#crée par xgbasai & Millanir
from tkinter import*
from random import randint


    #Liste de textes à lire
History=["000.txt","1.txt","2.txt","Screen.txt","11.txt","21.txt","12.txt","13.txt","22.txt"] ##Listes dans des listes?
HistImg=["concept_corpus.gif","Screen.gif"]

#Change la liste History en fonction du numéro
number=0

    #numéro de la salle
salle=0
choiSal=[] #Liste de liste pour changer de salle

    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)

health =healthMax
healthStr ="/"+str(healthMax)

    ##Simule un lancement de dès, réusittes/échecs


Objet=[] #Liste de none et de chiffres en fonction si on a ramassé un objet ou pas
item= 0 #Variable qui change en fonction de la salle
InvObj= 0
var=1



for i in range(0,10):
    Objet[i]= Objet.append(i)

def addObj():                   #Ajoute un objet à l'inventaire en fonction de la salle
    global item, Objet
    Objet[item] =1


def Inventory():                #Ouvre la fenêtre Inventaire
    fenInv = Tk()
    fenInv.title("Inventaire")
    fenInv.geometry("350x200")
    framinv = Frame(fenInv)
    def InvObj():
        framinv.destroy()
        if Objet[2] ==1:
            obj1= Message(framinv,text= "item quelconque",fg='black',width= "250")
            obj1.pack()
        if Objet[1] ==1:
            obj2= Message(framinv,text= "Lampe torche",width= "250")
            obj2.pack()
    boutan = Button(fenInv,width=8,text="Actualiser",command=InvObj)
    boutan.pack(side=BOTTOM)
    fenInv.mainloop()

#Change le texte et change les variables pour pouvoir avancer dans l'histoire
var1=1
var2=2
var3=3
def choix(var):
    Room[var]()

def machin(var):
    global can
    can.destroy()
    can = Frame(fram1, width =350, height =90, bg ='white')
    can.pack(padx =25, pady =20)
    guppy= open(History[var],'r', encoding= 'Utf-8')
    cod = guppy.read()
    guppy.close()
    tex4 = Message(can, text= cod,width=350,bg='white', fg= 'black')
    tex4.pack()

def room0():
    machin(0)
    var1= 2
    var2= 3
    var3= 1

def room1():
    machin(1)
    var1= 4
    var2= 5
    var3= 6

def room2():
    machin(2)
    var1= 3
    var2= 1
    var3= 2

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

Room=[room0,room1,room2]

guppy= open("000.txt",'r', encoding= 'Utf-8')
cod = guppy.read()
tex4 = Message(can, text= cod,width=350,bg='white', fg= 'black')
tex4.pack()
guppy.close()

fram2 = Frame(MainFrame,bg="gray",height=300,width=400)
fram2.pack(side=BOTTOM,padx=25,pady=20)

bou1 = Button(fram2, width=8, text="1",command=choix(var1))
bou1.pack()
bou1.grid(row= 0,column=0)

bou2=Button(fram2,width=8,text="2",command=choix(var2))
bou2.pack()
bou2.grid(row=0,column=1)

bou3=Button(fram2,width=8,text='3',command=choix(var3))
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
photo = PhotoImage(file =HistImg[salle])
item = canimg.create_image(150, 100, image =photo)




















fen1.mainloop ()

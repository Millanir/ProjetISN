# Créé par user, le 28/03/2017 en Python 3.2
#crée par xgbasai & Millanir
from tkinter import*
from random import randint


    #Liste de textes à lire
History=["000.txt","1.txt","2.txt","Screen.txt","11.txt","21.txt","12.txt","13.txt","22.txt"] ##Listes dans des listes?
HistImg=["concept_corpus.gif","Screen.gif"]
salle=0


    #Définit les stats
healthMax= randint(15,25)
luck= randint(25,75)
finesse=randint(3,10)

health =healthMax
healthStr ="/"+str(healthMax)

    ##Simule un lancement de dès, réusittes/échecs


Objet=[] #Liste de none et de chiffres en fonction si on a ramassé un objet ou pas
##item= 0 #Variable qui change en fonction de la salle
##InvObj= 0
##
##
##
##for i in range(0,10):
##    Objet[i]= Objet.append(i)


def Inventory():                #Ouvre la fenêtre Inventaire
    global framinv
    def refresh():
        fenInv.after(200,refresh)
        framinv.delete('all')
        framinv.create_text(25,25,text= Objet[item])

    fenInv = Tk()
    fenInv.title("Inventaire")
    fenInv.geometry("350x200")
    framinv= Canvas(fenInv)


    refresh()
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
    global var1,var2,var3
    machin(0)
    var1= 2
    var2= 3
    var3= 1


def room1():
    global var1,var2,var3
    machin(1)
    var1= 4
    var2= 5
    var3= 6

def room2():
    global var1,var2,var3
    machin(2)
    var1= 3
    var2= 1
    var3= 2

def screen():
    global var1,var2,var3
    machin(3)
    var1= 1
    var2= 2
    var3= 3

def room11():
    global var1,var2,var3
    machin(4)
    var1=1
    var2=2
    var3=3

def room12():
    global var1,var2,var3
    machin(6)
    var1=3
    var2=1
    var3=2

def room13():
    global var1,var2,var3,item
    machin(7)
    var1=2
    var2=3
    var3=1
    item= 0





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

Room=[room0,room1,room2,screen,room11,room12,room13]

guppy= open("000.txt",'r', encoding= 'Utf-8')
cod = guppy.read()
tex4 = Message(can, text= cod,width=350,bg='white', fg= 'black')
tex4.pack()
guppy.close()

fram2 = Frame(MainFrame,bg="gray",height=300,width=400)
fram2.pack(side=BOTTOM,padx=25,pady=20)

bou1 = Button(fram2, width=8, text="1",command=lambda: choix(var1))
bou1.pack()
bou1.grid(row= 0,column=0)

bou2=Button(fram2,width=8,text="2",command=lambda: choix(var2))
bou2.pack()
bou2.grid(row=0,column=1)

bou3=Button(fram2,width=8,text='3',command=lambda: choix(var3))
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
###KALKULACKA
###Lujza Milotova, 1. rocnik
###zimny semester 2021/2022
###PROGRAMOVANIE 1 NPRG030


#importovana kniznica tkinter na grafiku
from tkinter import *

#vyraz - vyraz, s ktorym budeme pracovat cely cas - na zaciatku prazdny string
vyraz=""
#vysledok - na zaciatku prazdny string, zapise sa donho vysledok po vyhodnoteni vyrazu
vysledok=""


#####FUNKCIE#####

#funkcie pre zadavanie cisel (z klavesnice alebo pomocou tlacidiel):
#kazda z funkcii pridava na koniec vyrazu (stringu) dany znak
#kazda z funkcii zaroven prepise na "displeji kalkulacky" vyraz na aktualny vyraz (vyraz s pridanym danym cislom)

def nula():
    global vyraz
    vyraz=vyraz+"0"
    L.configure(text=vyraz)

def jeden():
    global vyraz
    vyraz=vyraz+"1"
    L.configure(text=vyraz)

def dva():
    global vyraz
    vyraz=vyraz+"2"
    L.configure(text=vyraz)

def tri():
    global vyraz
    vyraz=vyraz+"3"
    L.configure(text=vyraz)

def styri():
    global vyraz
    vyraz=vyraz+"4"
    L.configure(text=vyraz)

def pat():
    global vyraz
    vyraz=vyraz+"5"
    L.configure(text=vyraz)

def sest():
    global vyraz
    vyraz=vyraz+"6"
    L.configure(text=vyraz)

def sedem():
    global vyraz
    vyraz=vyraz+"7"
    L.configure(text=vyraz)

def osem():
    global vyraz
    vyraz=vyraz+"8"
    L.configure(text=vyraz)

def devat():
    global vyraz
    vyraz=vyraz+"9"
    L.configure(text=vyraz)


#funkcie pre zadavanie operatorov (z klavesnice alebo pomocou tlacidiel):
#kazda z funkcii pridava na koniec vyrazu (stringu) znak daneho operatora
#kazda z funkcii zaroven prepise na "displeji kalkulacky" vyraz na aktualny vyraz (vyraz s pridanym danym operatorom)

def plus():
    global vyraz
    vyraz=vyraz+"+"
    L.configure(text=vyraz)

def minus():
    global vyraz
    vyraz=vyraz+"-"
    L.configure(text=vyraz)

def krat():
    global vyraz
    vyraz=vyraz+"×"
    L.configure(text=vyraz)

def deleno():
    global vyraz
    vyraz=vyraz+"÷"
    L.configure(text=vyraz)

def mocnina():
    global vyraz
    vyraz=vyraz+"^"
    L.configure(text=vyraz)


#funkcie pre zadavanie ostatnych znakov (z klavesnice alebo pomocou tlacidiel):
#(zadavnie zatvoriek a desatinnej ciarky)
#kazda z funkcii pridava na koniec vyrazu (stringu) dany znak
#kazda z funkcii zaroven prepise na "displeji kalkulacky" vyraz na aktualny vyraz (vyraz s pridanym danym znakom)

def zatvorka1():
    global vyraz
    vyraz=vyraz+"("
    L.configure(text=vyraz)

def zatvorka2():
    global vyraz
    vyraz=vyraz+")"
    L.configure(text=vyraz)

def desatinna_ciarka():
    global vyraz
    vyraz=vyraz+","
    L.configure(text=vyraz)


#funkcia pre zmazanie posledneho znaku z aktualneho vyrazu (z klavesnice alebo pomocou tlacidla):
#funkcia odstranuje posledny znak stringu vyrazu
#funkcia zaroven prepise na "displeji kalkulacky" vyraz na aktualny vyraz (vyraz s odobranym poslednym znakom)

def delete():
    global vyraz
    vyraz=vyraz[:-1]
    L.configure(text=vyraz)



### FUNKCIA PRE VYHODNOTENIE VYRAZU ###

def VYHODNOT():
    global vyraz,vysledok

    #prevod znakov × ÷ , na * / .
    vyraz0=list(vyraz)
    vyraz1=""
    
    for i in range(len(vyraz0)): #cyklus prechadza jednotlive znaky vyrazu a vybrane meni podla potreby (× ÷ , na * / .)
        if vyraz0[i]=="×":
            vyraz0[i]="*"
        elif vyraz0[i]=="÷":
            vyraz0[i]="/"
        elif vyraz0[i]==",":
            vyraz0[i]="."
        vyraz1+=vyraz0[i]

    #rozdelenie vyrazu na operandy a operatory
    infix=[]
    posledny=""
    for znak in vyraz1: #cyklus prechadza vyraz po znakoch a deli ho na casti - cisla (resp. desatiine cisla) a operandy
        if znak in "0123456789.":
            posledny+=znak #pridava cifry a desatinnu ciarku do samostatneho noveho stringu (aby kalkulacka vedela pracovat s viaccifernymi cislami a aj desatinnymi cislami)
        else:
            if posledny:
                infix.append(posledny)
                posledny = ""
            if znak:
                infix.append(znak)
    if posledny:
        infix.append(posledny)
   

    #overenie spravnosti uzatvorkovania zadaneho vyrazu
    z_vyraz=[i for i in vyraz]
    hodnota=0
    zasobnik=[]
    spravne=True
    for zatvorka in z_vyraz:
        if zatvorka=="(":
            hodnota+=1
            zasobnik.append("(")
        elif zatvorka==")":
            hodnota-=1
            if len(zasobnik)!=0:
                zasobnik.pop(-1)  
        if hodnota<0:
            spravne=False
            break    
    if hodnota!=0:
        spravne=False

    if spravne==False:
        L.configure(text="výraz je nesprávne uzátvorkovaný",font="Verdana 10")
        return


    #prevod vyrazu z infixovej notacie do postfixovej notacie pomocou zasobnika
    operatory=set(["+", "-", "*", "/", "(", ")", "^"]) #set operatorov a zatvoriek
    priorita={"+":1, "-":1, "*":2, "/":2, "^":3}  #priradenie priority jednotlivym operatorom pomocou slovnika
    zasobnik1=[] 
    postfix=[]
    for znak in infix: #cyklus prechadza postupne vyraz po znakoch
        if znak not in operatory:
            postfix.append(znak) #cisla (aj viacciferne aj desatinne) zapisuje rovno na vystup
        elif znak=="(": 
            zasobnik1.append("(") #lavu zatvorku dava do zasobnika
        elif znak==")":
            while zasobnik1 and zasobnik1[-1]!="(": #k pravej zatvorke hlada v zasobniku lavu
                postfix.append(zasobnik1.pop()) #kym najde prislusnu lavu zatvorku, tak zo zasobnika vybera znamienka a pise ich na vystup
            zasobnik1.pop()
        else:  
            while zasobnik1 and zasobnik1[-1]!="(" and priorita[znak]<=priorita[zasobnik1[-1]]:
                postfix.append(zasobnik1.pop()) #znamiemka vklada do zasobniku ale predtym odtial rusi a zapisuje na vystup znamienka s vyssou alebo rovnakou prioritou po najblizsiu lavu zatvorku
            zasobnik1.append(znak)
    while zasobnik1:
        postfix.append(zasobnik1.pop()) #na konci zo zasobnika vyberie a zapise na vystup vsekty zvysne znamienka


    #vyhodnotenie vyrazu v postfixovej notacii pomocou zasobnika
    zasobnik2=[]
    delenie_nulou=False #overenie, ci vyraz obsahuje delenie nulou je na zaciatku nastavene na False
    for znak in postfix: #cyklus prechadza posfixovy vyraz postupne po znakoch
        if znak not in operatory:
            zasobnik2.append(znak) #cisla (viacciferne aj desatinne) zapisuje rovno na vystup
        else: #so znamienkom prevedie danu operaciu s poslednymi dvoma cislami v zasobniku (tieto odtial odstrani) a vysledok zapise na koniec zasobnika
            if znak=="+":
                vysl=float(zasobnik2.pop())+float(zasobnik2.pop())
                zasobnik2.append(vysl)
            if znak=="*":
                vysl=float(zasobnik2.pop())*float(zasobnik2.pop())
                zasobnik2.append(vysl)
            if znak=="^":
                vysl=float(zasobnik2[-2])**float(zasobnik2[-1])
                zasobnik2.pop()
                zasobnik2.pop()
                zasobnik2.append(vysl)
            if znak=="-":
                vysl=float(zasobnik2[-2])-float(zasobnik2[-1])
                zasobnik2.pop()
                zasobnik2.pop()
                zasobnik2.append(vysl)
            if znak=="/":
                if float(zasobnik2[-1])==0: #overenie, ci po znaku delenia nenasleduje nula
                    delenie_nulou=True #ak nasleduje nula, tak vyraz sa neda vyhodnotit, nastavenie premennej na True
                else:
                    vysl=float(zasobnik2[-2])/float(zasobnik2[-1])
                    zasobnik2.pop()
                    zasobnik2.pop()
                    zasobnik2.append(vysl)
    if delenie_nulou:
        L.configure(text="nulou sa nedá deliť") #vypisanie chyboveho hlasenia o deleni nulou
        return #ukoncenie vyhodnocovania vyrazu, kedze sa vyraz neda vyhodnotit, lebo obsahuje delenie nulou
    else:
        cele=True #overenie, ci vyraz obsahuje iba cele cisla, nastavenie premmenej na True
        fin=zasobnik2[0]
        fin=list(str(fin))
        if "." in fin: #overime, ci vyraz obsahuje desatinnu ciarku
            index=fin.index(".")
            for i in range(index+1,len(fin)):
                if fin[i]!="0":
                    cele=False #ak je za desatinnou ciarkou cifra ina ako nula, tak vysledok je desatinne cislo, nastavenie premennej na False
                    break
        if cele==True: #ak je vysledok cele cislo, tak na displeji kalkulacky zobrazujeme vysledok typu int
            vysledok=int(zasobnik2[0])
            L1.configure(text=vysledok)
            vyraz=str(int(zasobnik2[0])) #do aktualneho vyrazu ukladame vysledok, aby sme s nim mohli dalej pracovat
        else: #ak vysledok nie je cele cislo, tak na displeji kalkulacky zobrazujeme vysledok typu float
            vysledok=(str(float(zasobnik2[0]))).replace(".",",") #nahradime znak "." znakom "," (tak to je bezne na kalkulackach)
            L1.configure(text=vysledok)
            vyraz=(str(zasobnik2[0])).replace(".",",") #do aktualneho vyrazu ukladame vysledok, aby sme s nim mohli dalej pracovat a spat nahradzame "," za ".", aby bol typ float citatelny
                


#####GRAFIKA#####

w=Tk()
w.title("Kalkulačka")

#pocet riadkov a stlpcov tlacidiel kalkulacky
r=7
s=4

#label, v ktorom vzdy vidime aktalny vyraz
#"displej kalkulacky"
L=Label(text=vyraz,font="Verdana 15")
L.grid(row=0,columnspan=s+1)

L1=Label(text=vysledok,font="Verdana 17")
L1.grid(row=1,columnspan=s+1)

#tlacidla pre zadavanie cifier
b0=Button(command=nula,text="0",font="Verdana 15",width=5)
b0.grid(row=r,column=s-2)
b1=Button(command=jeden,text="1",font="Verdana 15",width=5)
b1.grid(row=r-1,column=s-3)
b2=Button(command=dva,text="2",font="Verdana 15",width=5)
b2.grid(row=r-1,column=s-2)
b3=Button(command=tri,text="3",font="Verdana 15",width=5)
b3.grid(row=r-1,column=s-1)
b4=Button(command=styri,text="4",font="Verdana 15",width=5)
b4.grid(row=r-2,column=s-3)
b5=Button(command=pat,text="5",font="Verdana 15",width=5)
b5.grid(row=r-2,column=s-2)
b6=Button(command=sest,text="6",font="Verdana 15",width=5)
b6.grid(row=r-2,column=s-1)
b7=Button(command=sedem,text="7",font="Verdana 15",width=5)
b7.grid(row=r-3,column=s-3)
b8=Button(command=osem,text="8",font="Verdana 15",width=5)
b8.grid(row=r-3,column=s-2)
b9=Button(command=devat,text="9",font="Verdana 15",width=5)
b9.grid(row=r-3,column=s-1)

#tlacidla pre zadavanie operandov
bplus=Button(command=plus,text="+",font="Verdana 15",width=5,bg="MediumPurple1")
bplus.grid(row=r,column=s)
bminus=Button(command=minus,text="-",font="Verdana 15",width=5,bg="MediumPurple1")
bminus.grid(row=r-1,column=s)
bkrat=Button(command=krat,text="×",font="Verdana 15",width=5,bg="MediumPurple1")
bkrat.grid(row=r-2,column=s)
bdeleno=Button(command=deleno,text="÷",font="Verdana 15",width=5,bg="MediumPurple1")
bdeleno.grid(row=r-3,column=s)
bmocnina=Button(command=mocnina,text="^",font="Verdana 15",width=5,bg="MediumPurple1")
bmocnina.grid(row=r-4,column=s)

#tlacidla pre zadavnie zatvoriek a desatinnej ciarky
bz1=Button(command=zatvorka1,text="(",font="Verdana 15",width=5,bg="powderblue")
bz1.grid(row=r-4,column=s-3)
bz2=Button(command=zatvorka2,text=")",font="Verdana 15",width=5,bg="powderblue")
bz2.grid(row=r-4,column=s-2)
des_ciarka=Button(command=desatinna_ciarka,text=",",font="Verdana 15",width=5,bg="powderblue")
des_ciarka.grid(row=r,column=s-3)

#tlacidlo pre mazanie posledneho znaku z vyrazu
delet=Button(command=delete,text="del",font="Verdana 15",width=5,bg="powderblue")
delet.grid(row=r-4,column=s-1)

#tlacidlo "rovna sa", tlacidlo pre vyhodnotenie vyrazu
brovne=Button(command=VYHODNOT,text="=",font="Verdana 15",width=5,bg="aquamarine2")
brovne.grid(row=r,column=s-1)

#zviazanie klavesnice s funkciami, aby sme mohli zadavat cisla, operatory a ostatne znaky z klavesnice
c=Canvas()
c.bind_all("0",lambda event: b0.invoke())
c.bind_all("1",lambda event: b1.invoke())
c.bind_all("2",lambda event: b2.invoke())
c.bind_all("3",lambda event: b3.invoke())
c.bind_all("4",lambda event: b4.invoke())
c.bind_all("5",lambda event: b5.invoke())
c.bind_all("6",lambda event: b6.invoke())
c.bind_all("7",lambda event: b7.invoke())
c.bind_all("8",lambda event: b8.invoke())
c.bind_all("9",lambda event: b9.invoke())
c.bind_all("+",lambda event: bplus.invoke())
c.bind_all("-",lambda event: bminus.invoke())
c.bind_all("*",lambda event: bkrat.invoke())
c.bind_all("/",lambda event: bdeleno.invoke())
c.bind_all("^",lambda event: bmocnina.invoke())
c.bind_all(",",lambda event: des_ciarka.invoke())
c.bind_all("(",lambda event: bz1.invoke())
c.bind_all(")",lambda event: bz2.invoke())
c.bind_all("<BackSpace>",lambda event: delet.invoke())
#funkcia vyhodnotenia vyrazu je zviazana s klavesou "enter" aj s klavesou "rovna sa"
c.bind_all("=",lambda event: brovne.invoke())
c.bind_all("<Return>",lambda event: brovne.invoke())

w.mainloop()
#!/usr/bin/python3
import random


print("Zaczynam losowanie")

min=1
max=49
ileliczb=2;
maxLiczb=6;
ileLosowan=5;
c=0;

def losuj(min, max):
    liczby = []
    i = 0
    while i < ileliczb:
        liczba = random.randint(min, max)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby;

num1 = input('Start ')
wspolny=set();
licznikLosowan=0
aktualneLosowanie=0
while aktualneLosowanie<=maxLiczb:
    while licznikLosowan<=ileLosowan:
        wspolny=set();
        i=0
        zbior1=losuj(min, max)
       ## print("Zbior 1"+str(zbior1))
        while len(wspolny)!=ileliczb:
            zbior2=losuj(min, max)
            wspolny=set(zbior1)&set(zbior2)
            i=i+1;
            print("Losowanie nr"+str(i)+"   "+"Zbior 1"+str(zbior1)+"   Zbior 2"+str(zbior2))
            if(len(wspolny)==ileliczb):
                print(i)
                ##print("Trafione"+str(wspolny))
                licznikLosowan=licznikLosowan+1;
    else:
        print("Iloesc liczb "+str(ileliczb))
        aktualneLosowanie=aktualneLosowanie+1;
        licznikLosowan=0;
        ileliczb=ileliczb+1;

num2 = input('Ok')

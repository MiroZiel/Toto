#!/usr/bin/python3
import random


print("Zaczynam losowanie")

min=1
max=49
ileliczb=6;

def losuj(min, max):
    liczby = []
    i = 0
    while i < ileliczb:
        liczba = random.randint(min, max)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby;


wspolny=set();
i=0
while len(wspolny)!=ileliczb:
    zbior1=losuj(min, max)
    zbior2=losuj(min, max)
    wspolny=set(zbior1)&set(zbior2)
    i=i+1;
    if(len(wspolny)==ileliczb):
        print(i)
        print("Trafione"+str(wspolny))

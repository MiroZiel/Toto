#!/usr/bin/python3
import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
# print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))

liczby = []
# for i in range(ileliczb):
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1
print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
typy = set()
wylosowane = set()
i = 0
while i < ileliczb:
    typ = int(input("Podaj liczbę %s: " % (i + 1)))
    if typ not in typy:
        typy.add(typ)
        i = i + 1
        if typ in liczby:
            wylosowane.add(typ)



print("Wylosowane liczby:", liczby)

if wylosowane:
    print("\nIlość trafień: %s" % len(wylosowane))
    print("Trafione liczby: ", wylosowane)
else:
    print("Brak trafień. Spróbuj jeszcze raz!")
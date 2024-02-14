from random import *
from string import ascii_uppercase
#nimed = []
#for i in range(5):
#    nimi = input("Siseta nimi").capitalize()
#    nimed.append(nimi)
#print("loetelu oli",nimed)
#nimed.sort()
#print("Loetelu soorteeritud",nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep="")
#    print("vimane oli lisatud")
#uuedNimed = []
#for nimi in nimed:
#    if nimi not in uuedNimed:
#        uuedNimed.append(nimi)
#print(uuedNimed)
#õpilased = ['Juhan','Kati','mario','mario','mati','mati','mati']
#unikaalsedÕ = list(set(õpilased))
#print("unikaalne nimekiri", unikaalsedÕ)
#vanus=[1,13,18,33,55]
#minVanus = min(vanus)
#maxVanus = max(vanus)
#summa = sum(vanus)
#keskmine =summa/len(vanus)

#1

#arvud = []
#N = int(input("Mitu rida joonistame?"))
#S = input("siseta sumbol")
#for p in range(N):
#    arvud.append(randint(1,100))
#for p in range(N):
#    print(arvud[p]*S)
#2
#goroda = ['Tallsin', 'Narva,Narva-jõesuu', 'kohtla-järve', 'ida-Virumaa,Lääne-virumaa,Jõgevamaa', 
#          'Tartu linn','Tartumaa,Põlvamaa,Võrumaa,valgamaa',
#          "Viljandimaa,Järvamma,Harjumaa,Raplamaa","pärnumaa","Läänemaa,Hiumaa,Saremaa" ]
#while True:
#    while True:
#        try:
#            indeks = int(input("siseta viienumbriline indeksi"))
#            indeks_el_arv = len(str(indeks))
#            if indeks_el_arv == 5:
#                break

#            else:
#                print("on vaja 5 numbreline arv")
#        except:
#            print("Vale andmetüüp")
#    arv1 = indeks//10000
#    print(arv1)
#    arv2 = goroda[arv1-1]
#    if arv1 == 1 or 2 or 3:
#        print("sedi doma")
#    print(arv2) 
#    #symbolid = list(indeks)
#    #sym = symbolid[0]
#3
#spisok = []
#N = randint(2, 25)
#for i in range(N):
#    spisok.append(choice(ascii_uppercase))
#    print(spisok)
#kogus = int(input("Mitu elemendi vahetame oma vahel"))
#if len(spisok) // 2 >= kogus:
#    a = spisok[i]
#    spisok[i] = spisok[len(spisok)-i-1]
#    spisok[len(spisok) - 1 - i] = a
#4
#spisok = [9,7,1,4,5,6]
#maks = max(spisok)
#print("max arv ", maks)
#delenie = maks / len(spisok)
#spisok[0] = delenie
#print(spisok)

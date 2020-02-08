#Ćwiczenia python
#Utwórz program, który wypisuje listę słów w przypadkowej kolejności.
#Program powinien wypisać wszystkie słowa bez żadnych powtórzeń

#tworznie listy słów
slowa = ["pierwsze","drugie","trzecie","noga","oko","ucho","łokieć"]
import random

dlugosc = len(slowa)# przechowanie dlugosci listy
#pętla główna
for i in range(dlugosc):
    los=random.choice(slowa)#losowanie slowa
    print(los) #wyswietlenie losu
    slowa.remove(los)#usuwanie z listy elementów
    
##################################
   # adres = slowa.index(los) #przypisanie numeru indeksu listy
   # del slowa[adres]       #usuwanie wedlug indeksu z listy
    
        #Druga opcja usuwania przez indeksowanie

    
#############################################

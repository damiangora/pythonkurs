#Napisz program Kreator postaci do gry z podziałem na role.
#Gracz powinien otrzymać pulę 30 punktów, którą może spożytkować na cztery atrybuty:
#siła, zdrowie, mądrość i zręczność.
#Gracz powinien mieć możliwość przeznaczania punktów z puli na dowolny atrybut,
#jak również możliwość odbierania punktów przypisanych do atrybutu i przekazywania
#ich z powrotem do puli.

#Tworzymy list
postac=[["siła\t",0],["zdrowie",0],["mądrość",0],["zręczność",0],["pula\t",30]]
print("\n Witaj w kreatorze postaci \n")
import os # implikacja poleceń konsoli

loop=1    #definiowanie zmiennej wyboru
while loop != 0:#pętla główna
    #wypisywanie wartosci
    os.system("cls")
    print("\n Aktualne statystyki to : \n")
    for i in postac:
        print(i[0],"\t\t",i[1])
    #menu użytkownika
    print("""
                    1.edytuj siłę
                    2.edytuj zdrowię
                    3.edytuj mądrość
                    4.edytuj zręczność
                    0.wyjdź z kreatora\n""")
    loop=int(input('Co chcesz zrobić: '))

    
    if loop == 1:
        robocza=int(input("podaj ile siły chcesz dodać lub odjąć: "))
        if robocza >0 and robocza <= postac[4][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        elif robocza <0 and -robocza <= postac[0][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        else:
            input('zła wartość')
        
    elif loop == 2:
        robocza=int(input("podaj ile zdrowia chcesz dodać lub odjąć: "))
        if robocza >0 and robocza <= postac[4][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        elif robocza <0 and -robocza <= postac[0][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        else:
            input('zła wartość')

    elif loop == 3:
        robocza=int(input("podaj ile mądrości chcesz dodać lub odjąć: "))
        if robocza >0 and robocza <= postac[4][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        elif robocza <0 and -robocza <= postac[0][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        else:
            input('zła wartość')
        
    elif loop == 4:
        robocza=int(input("podaj ile zręczności chcesz dodać lub odjąć: "))
        if robocza >0 and robocza <= postac[4][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        elif robocza <0 and -robocza <= postac[0][1]:
            postac[loop-1][1]+=robocza
            postac[4][1]-=robocza
        else:
            input('zła wartość')

    elif loop == 0:
        if postac[4][1]==0:
            continue
        else:
            loop = 1
            print(" Nie rozdałeś wszystkich punktów")
            input("rozdaj punkty i mozesz zakonczyc")
            continue
        
    else:
        os.system("cls")
        print(" zła wartość")




#Koniec tworzenia
                
os.system("cls")
print("\n A więc twoja postać ma takie statystyki")
for i in postac:
    print(i[0],"\t\t",i[1])
input("nacisnij enter aby wyjść")

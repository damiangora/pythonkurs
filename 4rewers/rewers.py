#Utwórz program, który wczytuje komunikat użytkownika,
#a następnie wypisuje go w odwrotnej kolejności.

print(""" witam program wyświetający na odwrót tekst """)
#wczytanie tekstu
tekst =input('podaj swoj tekst: ')
#przypisanie do maxi długości
maxi=len(tekst)
#informacja o dłougości dla urzytkownika
print('tekst ma ',maxi,' znakow')
#pentla rosnąca z warunkiem końcowym podniesionym o 1
for i in range (1 ,maxi+1 , 1):
    #wyświetlenie wyniku poprzez zmiane znaku licznika
    print(tekst[-i], end="")
    

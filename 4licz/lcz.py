#Napisz program, który liczy za użytkownika. Umożliw użytkownikowi wprowadzenie
#liczby początkowej, liczby końcowej i wielkości odstępu między kolejnymi
#liczbami

print(" program licznik ")
mini = int(input('podaj minimum '))
maxi = int(input('podaj maximum '))
skok = int(input('podaj interwał '))

for i in range(mini, maxi, skok):
    print(i, end=" ")

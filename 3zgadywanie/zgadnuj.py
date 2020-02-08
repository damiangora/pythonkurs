#urzytkownik podaje liczbe kom ma ją odgadnąć
min =1
max =100
szukacz = 0
sukacz = int(szukacz)
i = 0
liczba = input("podaj liczbe od 1 do 100 ")
liczba = int(liczba)
szukacz = int(max //2)
while liczba != szukacz:
    i += i
    max = int(max //2)
    print(szukacz,max)
    if szukacz == liczba:
        break
    elif szukacz > liczba:
        szukacz = szukacz - max
    elif szukacz < liczba:
        szukacz = szukacz + max
    
    input()
print(szukacz," to szukana liczba")

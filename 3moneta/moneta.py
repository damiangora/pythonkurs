# program 100 razy rzuca monetą i podaje urzytkownikowi wynik
import random

i = int('0')
o = 0
r = 0
print("rzucamy 100 razy moneta")
while i != 100:
    m = random.randint(0,1)
    print(i,o,r,m)
    if m == 0:
        o += 1
    else:
        r += 1
    i += 1
print("wypadlo ",o,"orzelkow i",r," reszek")

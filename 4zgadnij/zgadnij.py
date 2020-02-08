#Utwórz grę, w której komputer wybiera losowo słowo, które gracz musi
#odgadnąć. Komputer informuje gracza, ile liter znajduje się w wybranym słowie.
#Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera jest
#zawarta w tym słowie. Komputer może odpowiedzieć tylko „tak” lub „nie”. Potem
#gracz musi odgadnąć słowo.
import random
zakres = ('krzeslo',
          'parapet',
          'hipopotam',
          'afryka',
          'europa')
wybrane = random.choice(zakres)
zgadula = ""
print('zgadnij slowo masz 5 szans na pytanie o litere')

for i in range(5):
    litera = input(' podaj litere : ')
    if litera.lower() in wybrane:
        print("ta litera tu jest")
    else:
         print("tej litery tu niema")
print(' a teraz zgadnij słowo jakie tu mamy')
while zgadula != wybrane:
    zgadula = input(' podaj slowo : ')
    if zgadula == wybrane:
        print('brawo wygrales')
        break

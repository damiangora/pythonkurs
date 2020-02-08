#Napisz program Sprzedawca samochodów, w którym użytkownik wprowadza podstawową
#cenę samochodu. Program powinien dodać szereg dodatkowych opłat, takich
#jak podatek, opłatę rejestracyjną, prowizję przygotowawczą dealera, opłatę
#za dostarczenie. Oblicz podatek i opłatę rejestracyjną jako pewien procent
#ceny podstawowej. Pozostałe opłaty powinny mieć stałe wartości. Wyświetl
#faktyczną cenę samochodu po doliczeniu wszystkich dodatków.
print("""              Witam
                     pomoge obliczyc wartosc auta
                      postepuj zgodnie z instrukcjami
""")
cena=float(input('\n podaj cene swojego cacka \n'))
vat = cena*0.23
skarbowka=cena*0.02
prowizja=float('100')
suma=vat+skarbowka+prowizja
print('furka kosztowala ',cena,'\n oplaty ',suma,' \n wsumie',cena+suma) 
input('\n enter koniec')

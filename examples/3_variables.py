#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Zmienne 
# - miejsca gdzie zapisujemy obliczone wartosci
# - min. by nie utracic wyniku obliczenia
wynik = 2 + 4 * 3

# Zagdnienie moze wydawac sie trywialne - nie mniej nie jest :)
# By dobrze zrozumieć co dzieje sie w tej jednej linijce musielibyśmy zdefiniować sobie:
# - pojęcie typu
# - system typowania w pythonie
# - zarządzanie pamięcią (garbage collection)
# - metody ewaluacji wyrażeń
# Niestety nie mamy na to czasu :(

# Tak więc postaramy się sprawnie i zwięźle przedstawić jak to wygląda w Pythonie:
# mając przykład
# var = 3 
# to co stoi po lewej stronie = będziemy nazywać "nazwą" lub zmienną
# to co po prawej, wartością.

# Zmienna/Nazwa nie zawiera informacji o typie.
# Wartość zawiera informacje o swoim typie.

# Do danej zmiennej możemy przypisać dowolne typy wartości.
# (inaczej niż w C++ czy Javie)

# Dla przykładu, powiedzmy że mamy zmienna var i kolejno wywołujemy na niej operacje:
# var = 1.0 
# var = 1
# var = "ala"
# Do tej samej zmiennej przypisujemy raz dane typu:
# zmiennoprzecinkowy
# całkowity
# string 

# Jest tak pięknie, tak łatwo, tak wygodnie.
# Dlaczego wszystkie jezyki programowania tak nie mają?
# Generalnie im wygodniejsze rzeczy oferuje język tym ma gorszą
# wydajność, i trudniej się w nim wykrywa błędy.


# Przypisywanie wartości do zmiennych:

# Jak można by się domyślać dzieje się to przy pomocy znaku =.
# Mając operacje var = 1
# to co mamy na lewo od = nazywa się "lvalue" (wartość lewostronna)
# a to co po prawej nazywa się "rvalue"

# By kod się mniej napracować i by kod był czytelniejszy dodano
# pochodne operatora przypisania:
# a+=2 # to samo co a=a+1
# a*=2 # to samo co a=a*2
# każda operacja artmetyczna ma swój odpowiednik: /= -= %= %= ** //= 


# Jak nazywać zmienne? - WAŻNE!
# Nasze programy mają być czytelne!
# - jeśli zmienna ma służyć przechowywaniu imion nazywamy ją:
# 	imie="ala" # nie aaa="ala"
# - nie stosujemy skrutów!
#	mc="wczesien"
#	lp="1" #chyba liczba pierwsze, ale moze tez liczba pojedyncza?
#	proc="12" #moe procent, moze numer procesu, moze cos z procesorem?
# - lepiej juz mieć dłuższą nazwę zmiennej (notacja wielbłądzia):
#	wspolczynnikTarciaDrewna # w koncu po to mamy nowoczesne edytory
#	#niz wszedzie pisac "wtd" czy moze "wTD".

# Konwencje/Kultura nazywania zmiennych:
# Programujac w danym jezyku należy się dowiedzieć 
# jaka nazywa się w nim zmienne.
# http://en.wikipedia.org/wiki/Identifier_naming_convention#Language-specific_conventions
# Różne są zasady dla oznaczania zmiennych, inne dla stałych inne dla funkcji itp.
# To czy pisząc w Pythonie wasz program wygląda jak program napisany w pythonie zależy od was!


# Najczęściej spotyka się notacje wielbłądzią:
# długaNazwaBliżejNiezidentyfikowanejZmiennej
# czy notacje z _
# długa_nazwa_blizej_niezidentyfikowanej_zmiennej

# Nie można dowolnie nazywać zmiennych:
# Legalne nazwy:
# - skladaja sie z liczb, malych i duzych liter oraz podkreslnika _
#	Hello_Wrold, hello_World, HelloWorld, He11oWor1d
# - nie moga zaczynac sie od liczb
#	3e11o_World
# 
# 
#


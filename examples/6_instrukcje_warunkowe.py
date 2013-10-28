#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# By móc rozmawiać o instrukcjach warunkowych 
# musimy wprowadzić typ bool który może mieć 2 wartości:
# True (duże T ważne!)
# False

# wszystkie wyrażenia typu:
# a > 3;
# a + 3 < 3;
# itp. ewoluują się do True lub False. 

liczba=5;
if liczba >= 10:
    print "Liczba jest większa lub równa 10"
else:
    print "Liczba jest mniejsza od 10"

# Czy bardziej rozbudowanie:
'''
liczba=5;
if liczba > 10:
    print "Liczba jest większa"
elif liczba == 10:
	print "Liczba rowna 10."
else:
    print "Liczba jest mniejsza od 10"
'''
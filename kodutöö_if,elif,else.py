#!/usr/bin/env python
#-*- coding: utf8 -*-

#Esimene ülesanne

tekst=raw_input("Sisesta mingi tekst: ")
if tekst.lower() in tekst and any(c.isdigit() for c in tekst):
	print "väiketähed ja numbrid"
elif tekst.lower() in tekst:
	print "väiketähed ja numbriteta"
elif tekst.upper() in tekst and any(c.isdigit() for c in tekst):
	print "suurtähed ja numbrid"
elif tekst.upper() in tekst:
	print "suurtähed"

	
#Teine ülesanne

number1=int(input("Sisesta esimene number: "))
number2=int(input("Sisesta teine number: "))
jagatav=3	
if number1 > number2:
	number1,number2 = number2,number1
number1 = number1 + (jagatav - (number1 % jagatav))
arvud= [i for i in range(number1,number2,jagatav)]
print "Esitatud numbrite vahel on "+ str(len(arvud)) + " arv, mis jaguvad kolmega"

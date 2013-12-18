#!/usr/bin/env python
#-*- coding: utf8 -*-
import sys
import time
#ette anda kursuri alguspunkt x ja y ja just sinna prindib ette antud teksti
"""
print "\033[y;xH" - viib kursori koordinaatidele x ja y
print "\033[2J" - ekraan tühjaks
"""

"""
def kursor(x, y, t):
	sys.stdout.write( "\033["+ str(y) + ";" + str(x) + "H" + t)

kursor(10, 20, "kollane")
sys.stdout.flush()

time.sleep(60)
"""

"""
ül
kasutades eelmises funktsioonis loodus kursori peoitsioneerimise ja teksti väljastamise
funktsiooni---
Loo uus funktsioon, mis väljastab ekraanile kasti servad. Funktsiooni parameetrid: x, y, w, h
"""



def kursor(x, y, t):
	sys.stdout.write( "\033["+ str(y) + ";" + str(x) + "H" + t)
	 
def box(x, y, w, h):
		kursor(x, y, "#"*x)
		kursor(x+w, y, "#")
		kursor(y, h, "#")
		kursor(x+w, w, "#")
		kursor(x, w, "#"*x)
		kursor(x+w, h, "#")


box(15, 20, 15, 20)
sys.stdout.flush()

time.sleep(60)



"""
def kursor(x, y, t):
	sys.stdout.write( "\033["+ str(y) + ";" + str(x) + "H" + t)
	 
def box(x, y, w, h):
		kursor(x, y, "#"*x)


box(15, 20, 70, 20)
sys.stdout.flush()

time.sleep(60)
"""

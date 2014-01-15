#!/usr/bin/env python
#-*- coding: utf8 -*-
import sys
import time

def kursor(x, y, t):
	sys.stdout.write( "\033["+ str(y) + ";" + str(x) + "H" + t)

def ruut(x, y, w, h):
	kursor(x, y, "#" *w)
	kursor(x, y+h, "#" *w)
	l=1
	while l < h:
		kursor(x, y+l, "#")
		kursor(x+w, y+l, "#")
		l=l+1
		
ruut(0, 20, 15, 3)
sys.stdout.flush()

time.sleep(60)

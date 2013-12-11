#!/usr/bin/env python
def ruut():
	w=int(input("Sisesta ruudu pikkus: "))
	h=int(input("Siseta ruudu laius: "))
	print "  "
	a=0
	c=0
	while a<w:
		d=0
		while d<h:
			d=d+1
			c=("#"*d)
		print c
		a=a+1

ruut()

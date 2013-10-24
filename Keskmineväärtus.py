from math import sqrt

def keskvaartus(n,x1,x2):
	return ((sqrt(x1**2 + x2**2)/2.))

print "keskvaartus= " + str(keskvaartus(2,3,4))

""

def rkv(x1,x2):
	return ((x1*x1+x2*x2)/2)**0.5
	
print "rkv=" + str(rkv(3,4))

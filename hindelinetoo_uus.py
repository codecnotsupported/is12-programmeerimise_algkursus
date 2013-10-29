#kahe arvu keskmine

def keskmine(a, b):
    return (a+b)/2.

print keskmine (3, 6)

print ""


#fibonacci jada

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print fibonacci(8)

print ""

#arvutab ruutvorrandi ja annab 2 vastust

from math import sqrt

def lahendus(a,b,c):
    ruut=b**2-4*a*c
    x1=(-b+sqrt(ruut))/2*a
    x2=(-b-sqrt(ruut))/2*a
    return x1, x2
    
print lahendus(1,9,4)


print "Keskmine"
print""
numbrid=[85.,133.]
keskmine = 0
sum = 0
for n in numbrid:
    sum = sum + n
    keskmine = sum / len(numbrid)
print keskmine

print"______________________________________"
print ""

print"Fibonacci jada"

def f(n):
    if n < 2:
        return n
    return f(n-2) + f(n-1)

print f(3)
print f(7)
print f(10)

print ""
print"______________________________________"
print"Ruutvrrand"

print ""
from math import sqrt


a=1
b=5
c=4



root1 = (-b +sqrt(b**2 - 4 * a *c))/2 * a
root2 = (-b -sqrt(b**2 - 4 * a *c))/2 * a
print root1, root2



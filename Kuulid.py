from random import randint
kuulid=['s']*5 +['m']*10 +['v']*15
print kuulid
print"_____________________________________"
i=randint(1,29)
kuul1=kuulid[i]
print kuul1
del kuulid[i]
print kuulid
kuulid=kuulid+[kuul1]
print kuulid
print"______________________________________________"
n=randint(1,29)
kuul2=kuulid[n]
print kuul2
del kuulid[n]
print kuulid
kuulid=kuulid+[kuul2]
print kuulid

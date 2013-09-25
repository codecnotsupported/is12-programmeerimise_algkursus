from random import randint
import random
kuulid=['s']*5 +['m']*10 +['v']*15
print kuulid
print"_____________________________________"
i=randint(1,29)
kuul1=kuulid[1]
print kuul1
del kuulid[i]
print kuulid
kuulid=kuulid+[kuul1]
print kuulid
print"______________________________________________"
kuul2=kuulid[i]
print kuul2
del kuulid[i]
print kuulid
kuulid=kuulid+[kuul2]
print kuulid

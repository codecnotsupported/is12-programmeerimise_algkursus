from random import randint
kuulid=['s']*5+['m']*10+['v']*15
erinevad=0
korrad=0
for i in xrange (100):
    max=len(kuulid)-1
    n=randint(0,max)
    kuul1=kuulid[n]
    del kuulid[n]
    
    max=len(kuulid)-1
    n=randint(0,max)
    kuul2=kuulid[n]
    del kuulid[n]
    
    if kuul1 != kuul2:
        erinevad=erinevad+1
    korrad=korrad+1
    
    kuulid=kuulid+[kuul1]
    kuulid=kuulid+[kuul2]

print 100*erinevad/korrad

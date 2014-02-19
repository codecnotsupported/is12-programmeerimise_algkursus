import sys

#a=['kollane', 'roheline', 'sinine', 'kolmas', 'neljas', 'koer', 'kass', 'lennuk', 'kass']


"""
append    - lisab mingi elemendi massiivi l6ppu juurde
insert    - lisab mingi elemendi juurde teatud asukohta massiivis  parint a.insert(2,'kolmas') - lisab asukohta 2 juurde s6na kolmas
remove    - eemaldab mingi elemendi massiivist
pop   	 - eemaldab mingi elemendi massiivist ja teatab sellest
index    - annab teada, kas otsitav on massiivis ja mitmendal kohal. Kui ei ole siis annab errori
count    - loeb mitu korda on mingit elementi massiivis
sort    - t6hestikuj6rjekorras massiiv
reverse    - tagant ette poole massiiv
"""


mangud=[
['Diablo2', 'action', 'offline'],
['Starcraft', 'strateegia', 'offline'],
['World of Warcraft', 'rpg', 'online'],
]

def add():
    lisamine=raw_input("Millist mangu soovite lisada?: ") 
    lisamine1=raw_input("Mis klassi kuulub?: ")
    lisamine2=raw_input("Kas offline voi online? ")
    lisatav =("['%s', '%s', '%s']") % (lisamine, lisamine1, lisamine2)
    mangud.append(lisatav)

    
def remove():
    eemaldus=int(raw_input("Mis nime soovita eemaldada?: "))
    mangud.remove(eemaldus)
    

    
def esita():
    for rida in mangud:
        print rida
   	 
def end():
    print "Head aega!"
    sys.exit()
    


def kasutaja():
    valik=raw_input("Mida sa soovid(lisa, naita, valja, eemalda): ")
    if valik=="lisa":
       add()
    elif valik=="naita":
        esita()
    elif valik=="valja":
        end()
    elif valik == "eemalda":
        remove()


while 1:
    kasutaja()

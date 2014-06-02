#!/usr/bin/env python
# -*- coding: utf-8 -*-

# selleks käima panemiseks on vaja installida ....espeak....

import os
import datetime

def tts(text):
      return os.system("espeak  -s 155 -a 200 "+text+" " )

m = raw_input("say something: ")
tts("'"+str(m)+"' ")


class Player:
    
    def createname(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def saying(self):
        "Tere tulemast mängu %s!" % self.name

        
        
mngja=Player()
mngja.createname(raw_input("Enter name: "))
mngja.saying()
tts("'"+str(mngja.saying)+"' ")



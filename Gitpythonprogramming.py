#!/usr/bin/env python
# -*- coding: utf-8 -*-

# selleks käima panemiseks on vaja installida ....espeak....

import os
import sys
import datetime

def tts(text):
      return os.system(" espeak -v en "+text+" --stdout|paplay " )

m = raw_input("say something: ")
tts("'"+str(m)+"'")
m = raw_input("say something: ")
tts("'"+str(m)+"'")

class Player:
    
    def createname(self, name):
        self.name = name

    def display_name(self):
        return self.name

    def saying(self):
        "Welcome to the game %s!" % self.name

        
        
mngja=Player() # Save slot for now I guess?
mngja.createname(raw_input("Guess a name or something?: "))
mngja.saying()


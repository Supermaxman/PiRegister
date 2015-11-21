import os, sys, select
from time import sleep
import RPi.GPIO as GPIO

class Button(object):
    def __init__(self, id):
        self.__input = False
        self.__previous = False
        self.__result = False
        self.__id = id
        GPIO.setup(self.__id, GPIO.IN)

    def getButtonBool(self):
        self.__input = GPIO.input(self.__id)
        
        if self.__input and self.__previous:
            self.__result = False
        else:
            self.__result = self.__input
        self.__previous = self.__input
        return self.__result
    def __streamEmpty(self):
        r, w, e = select.select([ self.__file ], [], [], 1)#TODO try shorter timeout
        val = False;
        if (self.__file not in r):
            val = True
        return val
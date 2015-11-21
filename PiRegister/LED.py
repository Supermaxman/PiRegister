import os, sys, select
from time import sleep
import RPi.GPIO as GPIO

class LED(object):
    def __init__(self, id):
        self.__id = id
        GPIO.setup(self.__id, GPIO.OUT)

    def blink(self):
        GPIO.output(self.__id, True)
        sleep(0.1)
        GPIO.output(self.__id, False)
        
    def setValue(self, value):
        GPIO.output(self.__id, value)

from Scanner import *
from Button import *
from LED import *
from Printer import *
from time import sleep
import RPi.GPIO as GPIO

class IOManager(object):
    def __init__(self):
        led = 11
        button = 13
        GPIO.setmode(GPIO.Board)
        GPIO.setup(led, GPIO.OUT)

        self.__scanner = Scanner()
        self.__button = Button(button)
        self.__led = LED(led)
        self.__printer = Printer()
        #set up connections and variables for button, light, printer, and scanner
    def getButton(self):
        return self.__button.getButtonBool()

    def getScan(self):
        return self.__scanner.getInput()

    def setLight(self, value):
        self.__led.setValue(value)
    def blinkLight(self):
        self.__led.blink()

    def printItem(self, item):
        self.__printer.printItem(item)
    def printComplete(self):
        self.__printer.complete()
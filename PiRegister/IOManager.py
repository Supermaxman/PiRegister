from Scanner import *

class IOManager(object):
    def __init__(self):
        self.scanner = Scanner()
        #set up connections and variables for button, light, printer, and scanner
    def getButton(self):
        #TODO: change this to actually work with the pi's button IO
        inpt = int(input("Button: "))
        if inpt == 1:
            return 1
        return 0
    def getScan(self):
        #TODO: change this to actually work with the scanner
        return self.scanner.getInput()
    def setLight(self, value):
        #TODO implement changing of light to set values
        return 0
    #def printItems(ItemReceipt
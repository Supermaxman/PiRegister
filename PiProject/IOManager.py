class IOManager(object):
    def __init__(self):
        #set up connections and variables for button, light, printer, and scanner
        return
    def getButton(self):
        #TODO: change this to actually work with the pi's button IO
        inpt = input("Button:") #Debugging work-around
        if inpt == "1":
            return 1
        return 0
    def getScan(self):
        #TODO: change this to actually work with the scanner
        inpt = input("Scan:") #Debugging work-around
        return int(inpt)
    def setLight(self, value):
        #TODO implement changing of light to set values
        return
    #def printItems(ItemReceipt
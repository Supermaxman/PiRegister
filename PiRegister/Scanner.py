import os, sys, select




class Scanner(object):
    def __init__(self):
        self.__file = open('/dev/hidraw0','rb')
        self.input = ""
    def getInput(self):
        self.input = ""
        loop = True
        inStr = ""
        if not self.__streamEmpty():
            buffer = os.read(self.__file.fileno(), 8)
            for c in buffer:
                if c > 0:
                    num = c - 29;
                    inStr += str(num)
            if self.__streamEmpty:
                loop = False
        self.input = inStr
        return int(self.input)
    def __streamEmpty():
        r, w, e = select.select([ self.__file ], [], [], 1)
        val = False;
        if (self.__file not in r):
            val = True
        return val
    #def printItems(ItemReceipt
import os, sys, select




class Scanner(object):
    def __init__(self):
        self.__file = open('/dev/hidraw0','rb')
        self.__input = ""
    def getInput(self):
        self.__input = ""
        inStr = ""

        while not self.__streamEmpty():
            buffer = os.read(self.__file.fileno(), 8)
            for c in buffer:
                if (c > 0):
                    inStr = inStr + str(c - 29)            
                print(c)
        self.__input = inStr
        return self.__input
    def __streamEmpty(self):
        r, w, e = select.select([ self.__file ], [], [], 1)
        val = False;
        if (self.__file not in r):
            val = True
        return val
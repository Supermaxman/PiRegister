import os, sys, select




class Scanner(object):
    def __init__(self):
        self.__file = open('/dev/hidraw0','rb')
        self.__input = "-1"
    def getInput(self):
        self.__input = "-1"
        inStr = "-1"
        if not self.__streamEmpty():
            buffer = os.read(self.__file.fileno(), 8)
            for c in buffer:
                if (c > 0):
                    inStr = str(c - 29)
                    break;
        self.__input = inStr
        return self.__input
    def __streamEmpty(self):
        r, w, e = select.select([ self.__file ], [], [], 1)
        val = False;
        if (self.__file not in r):
            val = True
        return val
import os, sys, select


#YOU DO NOT WANT TO KNOW HOW I FIGURED THIS OUT OK
hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }


class Scanner(object):
    def __init__(self):
        self.__file = open('/dev/hidraw0','rb')
        self.__input = ""
    def getInput(self):
        self.__input = ""
        inStr = ""
        shift = False
        while not self.__streamEmpty():
            buffer = os.read(self.__file.fileno(), 8)
            for c in buffer:
                if ord(c) > 0:
                    if shift: 
                        if int(ord(c)) == 2 :
                            shift = True
                        else:
                            inStr += hid2[ int(ord(c)) ]
                            shift = False       
                    else:
                        if int(ord(c)) == 2 :
                            shift = True
                        else:
                            inStr += hid[ int(ord(c)) ] 
        self.__input = inStr
        return self.__input
    def __streamEmpty(self):
        r, w, e = select.select([ self.__file ], [], [], 1)
        val = False;
        if (self.__file not in r):
            val = True
        return val
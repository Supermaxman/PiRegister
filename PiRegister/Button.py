import os, sys, select


class Button(object):
    def __init__(self):
        self.__file = open('/home/pi/Desktop/button.txt','rb')
        self.__input = False
        self.__previous = False
        self.__result = False
        #Just for development, needs to change for real button
    def getButtonBool(self):
        self.__input = False
        inStr = "0"
        if not self.__streamEmpty():
            buffer = os.read(self.__file.fileno(), 8)
            inStr = buffer
        if int(inStr) == 1:
            self.__input = True
        else:
            self.__input = False

        if self.__input and self.__previous:
            self.__result = False
        else:
            self.__result = self.__input
        self.__previous = self.__input
        return self.__result
    def __streamEmpty(self):
        r, w, e = select.select([ self.__file ], [], [], 1)
        val = False;
        if (self.__file not in r):
            val = True
        return val
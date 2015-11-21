import os, sys, select
from escpos import * 
from Item import *
#https://github.com/manpaz/python-escpos/wiki/Methods
class Printer(object):
    def __init__(self):
        self.__printer = printer.Usb(0x04b8,0x0202)

    def printItem(self, item):
        line = item.name
        name = item.name
        namelen = len(name)
        price = str(item.price)
        pricelen = len(price)
        maxname = 15
        maxprice = 6
        if namelen < (maxname):
            for i in range(namelen, (maxname + 1)):
                line += " "
        line += "  "
        if pricelen < (maxprice):
            for i in range(pricelen, (maxprice + 1)):
                line += " "
        line += price
        print(line)
        self.__printer.text(line)
    def complete(self):
        self.__printer.cut()
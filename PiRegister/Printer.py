import os, sys, select
from escpos import * 
#https://github.com/manpaz/python-escpos/wiki/Methods
class Printer(object):
    def __init__(self):
        self.__printer = printer.Usb(0x04b8,0x0202)

    def printItem(self, item):
        line = item.name
        name = item.name
        namelen = name.length
        price = str(item.price)
        pricelen = price.length
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
        self.__printer.text(line)
    def complete(self):
        self.__printer.cut()
import os, sys, select
from escpos import * 
from Item import *
#https://github.com/manpaz/python-escpos/wiki/Methods
class Printer(object):
    def __init__(self):
        self.__printer = printer.Usb(0x04b8,0x0202)

    def printHeader(self):
        self.__printer.set("CENTER", "B", "B", 2, 2)
        self.__printer.text("AllMart Receipt\n\n")

    def printItem(self, item):
        self.__printer.set("LEFT", "A", "normal", 1, 1)
        line = item.name
        name = item.name
        namelen = len(name)
        price = str(item.price)
        pricelen = len(price)
        maxname = 24
        maxprice = 6
        if namelen < (maxname):
            for i in range(namelen, (maxname + 1)):
                line += " "
        line += "  "
        if pricelen < (maxprice):
            for i in range(pricelen, (maxprice + 1)):
                line += " "
        line += (price + "\n")
        self.__printer.text(line)
    def printTotals(self, items):
        tax = 0.0825
        sub = 0

        for item in items:
            sub += item.price

        subtotal = Decimal(sub)
        
        taxtotal = Decimal(sub * tax)

        total = Decimal(subtotal + taxtotal)
        
        subStr = str(subtotal)
        subLen = len(subStr)
        taxStr = str(taxtotal)
        taxLen = len(taxStr)
        totalStr = str(total)
        totalLen = len(totalStr)

        maxCurrency = 6

        self.__printer.set("LEFT", "A", "B", 1, 1)
        line = "Subtotal                  "
        if subLen < (maxCurrency):
            for i in range(subLen, (maxCurrency + 1)):
                line += " "
        line += (subStr + "\n")

        line += "  Tax                     "
        if taxLen < (maxCurrency):
            for i in range(taxLen, (maxCurrency + 1)):
                line += " "
        line += (taxStr + "\n")

        line += "Total                     "
        if totalLen < (maxCurrency):
            for i in range(totalLen, (maxCurrency + 1)):
                line += " "
        line += (totalStr + "\n")
        self.__printer.text(line + "\n")
    def complete(self):
        self.__printer.cut()
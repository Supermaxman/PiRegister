from enum import Enum
import os

from Item import *
from IOManager import *

class State(Enum):
    waiting = 0
    loading = 1
    scanning = 2
    completed = 3
    processing = 4
    printing = 5


class CashRegister(object):
    #Object for main interface
    def __init__(self, filename):
        self.__io = IOManager()
        self.__load_items(filename)
        self.__take_input()#change to public function
    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, value):
        self.__items = value
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, value):
        self.__state = value
        print(value)
        #self.__io.setLight(self.__state)
        self.__io.blinkLight()
    def __load_items(self, filename):
        self.state = State.loading
        
        self.__lookup = {}
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, filename)
        with open(file_path) as itemFile:
            for line in itemFile:
                item = self.__parse(line)
                self.__lookup[item.id] = item

        self.state = State.waiting
    def __parse(self, line):
        strs = line.split(',')
        return Item(strs[0], strs[1], strs[2])
    def __take_input(self):
        self.state = State.waiting
        self.items = []
        while True: #loop for lifecycle, break when system shuts down or at other time when decided
            self.__read_button()
            if self.state == State.scanning:
                self.__scan_items()
            elif self.state == State.completed:
                self.__print_items()
                self.__cleanup()
    def __read_button(self):
        if self.__io.getButton():
            if self.state == State.waiting:
                self.state = State.scanning
            elif self.state == State.scanning or self.state == State.processing:
                self.state = State.completed
    def __scan_items(self):
        #write code based on how the scanner works
        #read from scanner, if value is not default value then go to State.processing
        #process id number from scanner, add to item list
        #process id number from scanner, add to item list
        #go to State.scanning when completed
        #write object interface if required for scanner use

        while self.state == State.scanning:
            scanStr = self.__io.getScan()
            if scanStr != "":
                self.state = State.processing
                #item = self.__lookup[scan]
                print(scanStr)
                #self.__add_item(item)
                self.state = State.scanning
            self.__read_button()

    def __add_item(self, item):
        tmp_items = self.items[:]
        for idx, itm in enumerate(self.items[:]):
            if itm.id == item.id:
                self.items[idx] = itm + item
                return
        self.items.append(item)
    def __print_items(self):
        #write code based on how the printer works
        #go to State.printing
        #print item list along with total values
        #go to State.waiting
        #write object interface if required for printer use
        #self.__io.printItems()
        self.state = State.printing
        for item in self.items:
            self.__io.printItem(item)
        self.__io.printComplete()
        self.state = State.waiting
    def __cleanup(self):
        self.items.clear()
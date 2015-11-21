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
        self.__take_input()

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
        while self.state == State.scanning:
            scanStr = self.__io.getScan()
            if scanStr != "":
                self.state = State.processing
                item = self.__lookup[int(scanStr)]
                print(item.id)
                self.__add_item(item)
                self.state = State.scanning
            self.__read_button()

    def __add_item(self, item):
        self.items.append(item)
    def __print_items(self):
        self.state = State.printing
        self.__io.printReceipt(self.items)
        self.state = State.waiting
    def __cleanup(self):
        self.items.clear()
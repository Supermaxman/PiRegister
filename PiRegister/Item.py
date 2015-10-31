from decimal import *

class Item(object):
    #Object for individual item data
    def __init__(self, id, name, price, units):
        self.id = id
        self.name = name
        self.price = price
        self.units = units
    @classmethod
    def fromunits(cls, units):
        return cls(cls.id, cls.name, cls.price, units)
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = int(value)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = str(value)
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = Decimal(value)
    @property
    def units(self):
        return self.__units
    @units.setter
    def units(self, value):
        value = int(value)
        if value >= 0:
            self.__units = value
        else:
            self.__units = 0
    def __str__(self):
        return "{0}:{1}:{2}:{3}".format(self.id, self.name, self.price, self.units)
    def __add__(self, other):
        return Item(self.id, self.name, self.price, self.units + other.units)

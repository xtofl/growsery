#!/usr/bin/python
"""
classes defining shopping list objects
"""
from collections import namedtuple


class Amount:
    def __init__(self, number, unit):
        self.number = number
        self.unit = unit

    def __eq__(self, other):
        return self.number == other.number and self.unit == other.unit

    def __add__(self, other):
        if other.number == 0:
            return self
        if self.number == 0:
            return other
        if(self.unit == other.unit):
            return Amount(self.number + other.number, self.unit)
        else:
            raise ArithmeticError("unit can't be added ({} + {})".format(self.unit, other.unit))

    def __rmul__(self, other):
        '''scalar multiplication'''
        assert isinstance(other, int) or isinstance(other, float)
        return Amount(self.number*other, self.unit)

Amount.zero = Amount(0, '')

Ingredient = namedtuple("Ingredient", ["name", "amount"])
Recipe = namedtuple("Recipe", ["for_people", "ingredients"])
Serving = namedtuple("Serving", ["recipe_name", "for_people"])

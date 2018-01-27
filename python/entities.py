#!/usr/bin/python
"""
classes defining shopping list objects
"""
from collections import namedtuple

Amount = namedtuple("Amount", ["number", "unit"])
Ingredient = namedtuple("Ingredient", ["name", "amount"])
Recipe = namedtuple("Recipe", ["for_people", "ingredients"])
Serving = namedtuple("Serving", ["recipe_name", "for_people"])

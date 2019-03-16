#!/usr/bin/python
"""
classes defining shopping list objects
"""
from collections import namedtuple
from functools import reduce


class Unit:
    def __init__(self, label, conversions=None):
        self.label = label
        self.conversions = dict(conversions) if conversions else {}
        self.conversions[self] = lambda x: x

    def to(self, other):
        return self.conversions[other]

    def __repr__(self):
        return "<{}>".format(self.label)

    def __str__(self):
        return self.label


class Amount:
    def __init__(self, number, unit):
        assert isinstance(unit, Unit), "'{}:{}' is not a Unit".format(unit, unit.__class__)
        self.number = number
        self.unit = unit

    def __eq__(self, other):
        return self.number == other.number and self.unit == other.unit

    def __add__(self, other):
        assert isinstance(other, self.__class__), "adding {} + {}".format(self, other)
        if other.number == 0:
            return self
        if self.number == 0:
            return other
        try:
            try:
                return Amount(self.number + other.unit.to(self.unit)(other.number), self.unit)
            except KeyError:
                return Amount(self.unit.to(other.unit)(self.number) + other.number, other.unit)
        except KeyError:
            raise ArithmeticError("unit can't be added ({} + {})".format(self.unit, other.unit))

    def __sub__(self, other):
        return self + (-1 * other)
    def __rmul__(self, other):
        '''scalar multiplication'''
        assert isinstance(other, int) or isinstance(other, float)
        return Amount(self.number*other, self.unit)

    def __hash__(self):
        return hash((self.number, self.unit))

Amount.zero = Amount(0, Unit("any"))
Amount.__repr__ = lambda self: "{} {}".format(self.number, self.unit)

Ingredient = namedtuple("Ingredient", ["name", "amount"])
Ingredient.__repr__ = lambda self: self.name + ": " + repr(self.amount)
Ingredient.__rmul__ = lambda self, f: Ingredient(self.name, f * self.amount)
Ingredient.zero = lambda self: Ingredient(self.name, Amount(0, self.amount.unit))
Ingredient.__add__ = lambda self, other: self.name == other.name and Ingredient(self.name, self.amount + other.amount)

class IngredientList:
    def __init__(self, ingredients):
        self.ingredients = frozenset(ingredients)

    def __add__(self, other):
        if other == self.zero:
            return self
        if self == self.zero:
            return other
        set1 = dict((i.name, i) for i in self.ingredients)
        set2 = dict((i.name, i) for i in other.ingredients)
        all_dicts = [set1, set2]
        all_keys = tuple(reduce(lambda r, x: r.union(set(x)), map(dict.keys, all_dicts), set()))

        def summed(key):
            ingredients = filter(lambda x: x, (d.get(key, None) for d in all_dicts))
            amounts = list(i.amount for i in ingredients)
            try:
                return Ingredient(name=key, amount=sum(amounts, Amount.zero))
            except ArithmeticError as e:
                raise ArithmeticError("{}: {}".format(key, e))


        return IngredientList(summed(key) for key in all_keys)

    def __sub__(self, other):
        return self + (-1 * other)
    
    def __repr__(self):
        return "I[" + ", ".join(map(repr, self.ingredients)) + "]"

    def __eq__(self, other):
        return self.ingredients == other.ingredients

    def __iter__(self):
        return iter(self.ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __rmul__(self, f):
        return IngredientList(f * i for i in self.ingredients)

IngredientList.zero = IngredientList([])

Recipe = namedtuple("Recipe", ["for_people", "ingredients"])
Serving = namedtuple("Serving", ["recipe", "for_people"])

class CompoundRecipe:
    def __init__(self, for_people, recipes):
        self.for_people = for_people
        self.recipes = list(recipes)

    @property
    def ingredients(self):
        lists = (((self.for_people/float(x.for_people)) * IngredientList(x.ingredients)) for x in self.recipes)
        return sum(lists, IngredientList.zero)

    def __repr__(self):
        return "Compound {}".format(self.recipes)

    def __eq__(self, other):
        lhs, rhs = self, other
        return lhs.for_people == other.for_people and lhs.recipes == rhs.recipes

def for_people(n):
    """fluid interface to instantiate recipes

    >>> for_people(5).serve(Recipes.pasta, Recipes.bolognese)
    """
    def compound(*recipes):
        return Serving(CompoundRecipe(
            for_people=n, recipes=list(recipes)),
            for_people=n)
    compound.serve = compound
    return compound

def test_for_people():
    x = Ingredient("x", Amount(1, Unit(".")))
    y = Ingredient("y", Amount(2, Unit("-")))
    recipe = Recipe(5, [x, y])
    serving = for_people(10).serve(recipe)
    assert serving == Serving(
        for_people=10,
        recipe=CompoundRecipe(for_people=10, recipes=[recipe]))

#!/usr/bin/python
"""
a system to extract a shopping list from a week menu
"""

import sys
from collections import Counter
from functools import reduce

from entities import *
from data import recipes, menu, pantry, conversions, extras


def ingredient(name, amount, unit="stuk"):
    return Ingredient(name, Amount(amount, unit))


def make_convertor(conversions):
    def tryconvert(a, b):
        c = (a.unit, b.unit)
        if c in conversions:
            return conversions[c](a)
        else:
            return None

    return tryconvert


def subtract_amount(lhs, rhs, conversions):
    tryconvert = make_convertor(conversions)
    rhs = tryconvert(rhs, lhs) or rhs
    lhs = tryconvert(lhs, rhs) or lhs
    assert lhs.unit == rhs.unit, "{} != {}".format(lhs.unit, rhs.unit)
    return Amount(lhs.number - rhs.number, lhs.unit)


def add_amount(lhs, rhs, conversions):
    tryconvert = make_convertor(conversions)
    rhs = tryconvert(rhs, lhs) or rhs
    lhs = tryconvert(lhs, rhs) or lhs
    assert lhs.unit == rhs.unit, "{} != {}".format(lhs.unit, rhs.unit)
    return Amount(lhs.number + rhs.number, lhs.unit)


def sum_amounts(conversions, amounts):
    zero = Amount(0, next(iter(amounts)).unit)
    return reduce(lambda r, amount: add_amount(r, amount, conversions), amounts, zero)


def join_ingredients(list1, list2, conversions):
    set1 = dict((i.name, i) for i in list1)
    set2 = dict((i.name, i) for i in list2)
    all_dicts = [set1, set2]
    all_keys = tuple(reduce(lambda r, x: r.union(set(x)), map(dict.keys, all_dicts), set()))

    def summed(key):
        ingredients = filter(lambda x: x, (d.get(key, None) for d in all_dicts))
        amounts = list(i.amount for i in ingredients)
        return Ingredient(name=key, amount=sum_amounts(conversions, amounts))
    return [summed(key) for key in all_keys]


def subtract_ingredients(list1, list2, conversions):
    def subtract_amount_in_list2(amount, name):
        try:
            amount2 = next(i for i in list2 if i.name == name).amount
            return subtract_amount(amount, amount2, conversions)
        except StopIteration:
            return amount
    return list(i for i in
            (Ingredient(
                ingredient.name,
                subtract_amount_in_list2(ingredient.amount, ingredient.name))
            for ingredient in list1) if i.amount.number > 0)


def needed_ingredients(servings, recipes):
    def serve(s):
        return serve_for(s.for_people, recipes[s.recipe_name])
    dishes = [serve(s) for s in servings]
    # todo: noe duplicate ingredients!
    all = [ingredient
        for dish in dishes
        for ingredient in dish.ingredients]
    names = [i.name for i in all]
    d = {}
    for i in all:
        if i.name in d:
            d[i.name] = Ingredient(i.name, Amount(
                d[i.name].amount.number + i.amount.number,
                d[i.name].amount.unit
            ))
        else:
            d[i.name] = i
    return d.values()


def resulting_list(menu, recipes, pantry, conversions):
    dishes = menu
    ingredients_needed = needed_ingredients(menu, recipes)
    results = subtract_ingredients(ingredients_needed, pantry, conversions)
    return filter(lambda r: r.amount.number > 0, results)

def serve_for(for_people, recipe):
    scale = for_people / float(recipe.for_people)
    def scale_ingredient(i):
        return Ingredient(i.name, Amount(i.amount.number * scale, i.amount.unit))
    return Recipe(
        for_people=for_people,
        ingredients=list(map(scale_ingredient, recipe.ingredients))
    )

def print_ingredients(ingredients):
    for ingredient in sorted(ingredients, lambda i, j: i.name < j.name):
        print("{0:<20}: {1:>6} {2}".format(
            ingredient.name,
            ingredient.amount.number,
            ingredient.amount.unit))


def main():
    if "-v" in sys.argv:
        print("needed ingredients")
        print_ingredients(needed_ingredients(menu, recipes))
    shopping_list_menu = resulting_list(menu, recipes, pantry, conversions)
    shopping_list = join_ingredients(shopping_list_menu, extras, conversions)
    print("\nshopping list")
    print_ingredients(shopping_list)

if __name__ == "__main__":
    main()
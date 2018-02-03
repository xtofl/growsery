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
    return lhs + (-1 * rhs)


def add_amount(lhs, rhs, conversions):
    tryconvert = make_convertor(conversions)
    rhs = tryconvert(rhs, lhs) or rhs
    lhs = tryconvert(lhs, rhs) or lhs
    assert lhs.unit == rhs.unit, "{} != {}".format(lhs.unit, rhs.unit)
    return lhs + rhs


def sum_amounts(conversions, amounts):
    return sum(amounts, Amount.zero)


def join_ingredients(list1, list2):
    return IngredientList(list1) + IngredientList(list2)


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
            d[i.name] = Ingredient(i.name, d[i.name].amount + i.amount)
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
        return Ingredient(i.name, scale * i.amount)
    return Recipe(
        for_people=for_people,
        ingredients=list(map(scale_ingredient, recipe.ingredients))
    )

def print_ingredients(ingredients):
    for ingredient in sorted(ingredients, key=lambda i: i.name):
        print("{0:<20}: {1:>6} {2}".format(
            ingredient.name,
            ingredient.amount.number,
            ingredient.amount.unit))


def main():
    if "-v" in sys.argv:
        print("needed ingredients")
        print_ingredients(needed_ingredients(menu, recipes))
    shopping_list_menu = resulting_list(menu, recipes, pantry, conversions)
    shopping_list = join_ingredients(shopping_list_menu, extras)
    print("\nshopping list")
    print_ingredients(shopping_list)

if __name__ == "__main__":
    main()
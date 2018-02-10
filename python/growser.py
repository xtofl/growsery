#!/usr/bin/python
"""
a system to extract a shopping list from a week menu
"""

import sys

from entities import *
from data import Recipes, menu, pantry, extras


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


def subtract_amount(lhs, rhs):
    return lhs + (-1 * rhs)


def add_amount(lhs, rhs):
    return lhs + rhs


def sum_amounts(amounts):
    return sum(amounts, Amount.zero)


def join_ingredients(list1, list2):
    return IngredientList(list1) + IngredientList(list2)


def subtract_ingredients(list1, list2):
    def subtract_amount_in_list2(amount, name):
        try:
            amount2 = next(i for i in list2 if i.name == name).amount
            return subtract_amount(amount, amount2)
        except StopIteration:
            return amount
    return list(i for i in
            (Ingredient(
                ingredient.name,
                subtract_amount_in_list2(ingredient.amount, ingredient.name))
            for ingredient in list1) if i.amount.number > 0)


def needed_ingredients(servings):
    def serve(s):
        assert isinstance(s, Serving), s
        return serve_for(s.for_people, s.recipe)
    dishes = [serve(s) for s in servings]
    # todo: noe duplicate ingredients!
    all = [IngredientList(dish.ingredients) for dish in dishes]
    return sum(all, IngredientList.zero)


def resulting_list(menu, pantry):
    ingredients_needed = needed_ingredients(menu)
    results = ingredients_needed - IngredientList(pantry)
    return filter(lambda r: r.amount.number > 0, results)


def serve_for(for_people, recipe):
    assert isinstance(recipe, Recipe) or isinstance(recipe, CompoundRecipe), recipe
    scale = for_people / float(recipe.for_people)
    def scale_ingredient(i):
        return scale * i
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
        print_ingredients(needed_ingredients(menu))
    shopping_list_menu = resulting_list(menu, pantry)
    shopping_list = join_ingredients(shopping_list_menu, extras)
    print("\nshopping list")
    print_ingredients(shopping_list)

if __name__ == "__main__":
    main()
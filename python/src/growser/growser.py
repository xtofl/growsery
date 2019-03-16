#!/usr/bin/env python3
"""
a system to extract a shopping list from a week menu
"""

import sys

from .entities import *
from math import ceil
import growser.shop
from .pantry import from_pantry
from .pantry import from_file as pantry_from_file
import argparse

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
    scale = float(for_people) / float(recipe.for_people)
    def scale_ingredient(i):
        return scale * i
    return Recipe(
        for_people=for_people,
        ingredients=list(map(scale_ingredient, recipe.ingredients))
    )

def amount_str(amount):
    return "{0:<6.0f} {1:<2}".format(
            ceil(amount.number),
            str(amount.unit))

def parse_options():
    parser = argparse.ArgumentParser(description="growser - a growing grocery list")
    parser.add_argument("-v", action="store_true", dest="verbose")
    parser.add_argument("--pantry", type=str, dest="pantry_file", default="pantry.txt")
    parser.add_argument("--show_pantry", action="store_true", dest="show_pantry")
    parser.add_argument("--shop", type=str, default="shop.txt")
    return parser.parse_args()

def print_ingredients(ingredients, pantry=None, shop=None):
    print("      {0:<20}  {1} (-{2})".format(
            "ingredient.name",
            "amount",
            "in_pantry amount"))
    if shop:
        key = lambda i: shop.index(i.name)
    else:
        key = lambda i: i.name
    for ingredient in sorted(ingredients, key=key):
        in_pantry = from_pantry(pantry, ingredient) if pantry else None
        if in_pantry:
            print("    o {0:<20}: {1} (-{2} {3})".format(
                ingredient.name,
                amount_str(ingredient.amount),
                in_pantry.amount.number,
                in_pantry.amount.unit))
        else:
            print("    O {0:<20}: {1}".format(
                ingredient.name,
                amount_str(ingredient.amount)))

def print_shopping_list(options, data):
    if options.verbose:
        print("menu")
        for dish in data.menu:
            print("dish: ")
            print(dish)
        print("needed ingredients")
    if options.show_pantry:
        print_ingredients(needed_ingredients(data.all_dishes), data.pantry)
    shopping_list_menu = resulting_list(data.all_dishes, data.pantry)
    shopping_list = join_ingredients(shopping_list_menu, data.extras)
    title = "shopping list for {} dishes".format(len(data.menu))
    line = "- "*(len(title)//2+1)
    print("\n{}\n{}".format(title, line))
    if options.shop:
        the_shop = growser.shop.from_file(open(options.shop, "r"))
    else:
        the_shop = None
    print_ingredients(shopping_list, shop=the_shop)
    summary = "{} items for {} dishes".format(
        len(shopping_list),
        len(data.menu))
    print(summary)

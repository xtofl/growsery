#!/usr/bin/python
"""
a system to extract a shopping list from a week menu
"""

import sys
from entities import *
from data import recipes, menu, pantry


def ingredient(name, amount, unit="stuk"):
    return Ingredient(name, Amount(amount, unit))


def subtract_amount(lhs, rhs):
    assert lhs.unit == rhs.unit
    return Amount(lhs.number - rhs.number, lhs.unit)


def subtract_pantry(ingredient, pantry):
    try:
        p = next(i for i in pantry if i.name == ingredient.name)
        return Ingredient(
            ingredient.name,
            subtract_amount(ingredient.amount, p.amount))
    except:
        return Ingredient(ingredient.name + "?", ingredient.amount)


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


def resulting_list(menu, recipes, pantry):
    dishes = menu
    ingredients_needed = needed_ingredients(menu, recipes)
    results = [\
        subtract_pantry(i, pantry)\
        for i in ingredients_needed]
    return filter(lambda r: r.amount.number > 0, results)

def serve_for(for_people, recipe):
    scale = for_people / float(recipe.for_people)
    def scale_ingredient(i):
        return Ingredient(i.name, Amount(i.amount.number * scale, i.amount.unit))
    return Recipe(for_people=for_people,
        ingredients=map(scale_ingredient, recipe.ingredients)
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
    shopping_list = resulting_list(menu, recipes, pantry)
    print("\nshopping list")
    print_ingredients(shopping_list)

if __name__ == "__main__":
    main()
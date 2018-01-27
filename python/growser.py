#!/usr/bin/python

from flask import Flask
from collections import namedtuple

Amount = namedtuple("Amount", ["number", "unit"])
Ingredient = namedtuple("Ingredient", ["name", "amount"])

basis_recipes = {
    "witte saus": [
        Ingredient("bloem", Amount(50, "gram")),
        Ingredient("bakboter", Amount(1, "beetje")),
        Ingredient("melk", Amount(.8, "liter")),        
    ]
}

Recipe = namedtuple("Recipe", ["for_people", "ingredients"])

recipes = {
    "papaschotel":
        Recipe(for_people=5, ingredients=[
            Ingredient("witte kool", Amount(.5, "stuks")),
            Ingredient("gehakt", Amount(500, "gram"))]),
    "salade met eitjes en ovenschotel met pasta en tomatensaus":
        Recipe(for_people=5, ingredients=[
            Ingredient("ijsbergsla", Amount(0.3, "krop")),
            Ingredient("ei", Amount(6, "stuks")),
            Ingredient("krulletjes", Amount(500, "gram")),
            Ingredient("tomatenconcentraat", Amount(2, "blikjes")),
        ] + basis_recipes["witte saus"]),
    "balletjes tomatensaus met boontjes":
        Recipe(for_people=5, ingredients=[
            Ingredient("gehakt", Amount(500, "gram")),
            Ingredient("boontjes", Amount(2, "pakjes")),
            ] + basis_recipes["witte saus"] + [
            Ingredient("tomatenconcentraat", Amount(2, "blikjes")),
        ]),
    "pasta bolognese": Recipe(for_people=5, ingredients=[]),
    "kip met currysaus, perziken en patatten": Recipe(for_people=5, ingredients=[]),
}


menu = {
    "zaterdag": "papaschotel",
    "zondag": "salade met eitjes en ovenschotel met pasta en tomatensaus",
    "maandag": "balletjes tomatensaus met boontjes",
    "dinsdag": "pasta bolognese",
    "woensdag": "kip met currysaus, perziken en patatten"
}

pantry = [
    Ingredient("pasta", Amount(1, "pak")),
    Ingredient("gehakt", Amount(500, "gram")),
]

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


def needed_ingredients(dishes, recipes):
    return [ingredient
        for dish in dishes
        for ingredient in recipes[dish].ingredients]


def resulting_list(menu, recipes, pantry):
    dishes = menu.values()
    ingredients_needed = needed_ingredients(menu.values(), recipes)
    results = [\
        subtract_pantry(i, pantry)\
        for i in ingredients_needed]
    return results

def print_ingredients(ingredients):
    for ingredient in ingredients:
        print("{0:<20}: {1:<4} {2}".format(
            ingredient.name,
            ingredient.amount.number,
            ingredient.amount.unit))

def main():
    shopping_list = resulting_list(menu, recipes, pantry)
    print("shopping list")
    print_ingredients(shopping_list)

if __name__ == "__main__":
    main()
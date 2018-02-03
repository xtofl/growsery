"""tests for the growser script"""
from functools import reduce
from operator import add

import pytest

from entities import Recipe, Ingredient, Amount, Serving
import growser

recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, "."))])

def test_recipe_amount_for_more_people():
    scaled = growser.serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2



def test_needed_ingredients_from_menu_are_accumulated():
    recipes = {
        "dish1": Recipe(1, [
            Ingredient("x", Amount(1, ".")),
            Ingredient("y", Amount(1, "-"))]),
        "dish2": Recipe(1, [
            Ingredient("y", Amount(1, "-")),
            Ingredient("z", Amount(1, "*"))])
    }
    servings = [
        Serving("dish1", 2),
        Serving("dish2", 3)
    ]
    ingredients = growser.needed_ingredients(servings, recipes)
    assert len(ingredients) == 3
    def amount_for(name):
        return next(i for i in ingredients if i.name == name).amount
    assert amount_for("x") == Amount(2, ".")
    assert amount_for("y") == Amount(5, "-")
    assert amount_for("z") == Amount(3, "*")


def test_pantry_is_subtracted_from_need():
    need = [
        Ingredient("x", Amount(10, ".")),
        Ingredient("y", Amount(10, "-"))
    ]
    assert len(growser.subtract_ingredients(need, need, {})) == 0
    assert growser.subtract_ingredients(need, [], {}) == need
    result = growser.subtract_ingredients(need, [Ingredient("y", Amount(5, "-"))], {})
    def amount_for(name):
        return next(i for i in result if i.name == name).amount
    assert amount_for("x") == Amount(10, ".")
    assert amount_for("y") == Amount(5, "-")


def test_unit_conversion():
    conversions = {
        ("kg", "g"): lambda x: Amount(1000 * x.number, "g")
    }
    def test(a1, u1, a2, u2):
        return growser.subtract_amount(Amount(a1, u1), Amount(a2, u2), conversions)
    assert test(1, "kg", 1, "g") == Amount(999, "g")
    assert test(1001, "g", 1, "kg") == Amount(1, "g")


def test_amounts_behave_as_monoid():
    assert growser.add_amount(Amount(5, '='), Amount(10, '='), []) == Amount(15, '=')
    assert growser.sum_amounts([], [Amount(5, '='), Amount(10, '=')]) == Amount(15, '=')
    a = Amount(5, '=')
    b = Amount(10, '=')
    c = Amount(3, '=')
    assert a + b == Amount(15, '=')
    with(pytest.raises(ArithmeticError)):
        a + Amount(10, '*')
    assert a + Amount.zero == a
    assert Amount.zero + a == a
    assert (a + b) + c == a + (b + c)

    assert reduce(add, (a, b, a, b), Amount.zero) == Amount(30, '=')




def test_ingredient_lists_can_be_added():
    x = growser.ingredient("x", 1, ".")
    y = growser.ingredient("y", 1, "-")
    assert x in growser.join_ingredients([x], [y], [])
    assert y in growser.join_ingredients([x], [y], [])
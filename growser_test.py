"""tests for the growser script"""
from functools import reduce
from operator import add

import pytest

from entities import Recipe, Ingredient, Amount, Serving, Unit, CompoundRecipe
import growser


class U:
    r = Unit("r")
    s = Unit("s")
    t = Unit("t")

recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, U.r))])
recipe2 = Recipe(for_people=1, ingredients=[
    Ingredient("x", Amount(1, U.r)),
    Ingredient("y", Amount(2, U.s))
    ])

def test_recipe_amount_for_more_people():
    scaled = growser.serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2

def extract_amounts(ingredient_list, ingredient_names):
    return map(lambda name: next(i for i in ingredient_list if i.name == name).amount, ingredient_names)

def test_needed_ingredients_from_menu_are_accumulated():
    dish1 = Recipe(1, [
        Ingredient("x", Amount(1, U.r)),
        Ingredient("y", Amount(1, U.s))])
    dish2 = Recipe(1, [
        Ingredient("y", Amount(1, U.s)),
        Ingredient("z", Amount(1, U.t))])
    servings = [
        Serving(dish1, 2),
        Serving(dish2, 3)
    ]
    ingredients = growser.needed_ingredients(servings)
    assert len(ingredients) == 3
    x, y, z = extract_amounts(ingredients, "xyz")
    assert x == Amount(2, U.r)
    assert y == Amount(5, U.s)
    assert z == Amount(3, U.t)


def test_pantry_is_subtracted_from_need():
    need = [
        Ingredient("x", Amount(10, U.r)),
        Ingredient("y", Amount(10, U.s))
    ]
    assert len(growser.subtract_ingredients(need, need)) == 0
    assert growser.subtract_ingredients(need, []) == need
    result = growser.subtract_ingredients(need, [Ingredient("y", Amount(5, U.s))])
    x, y = extract_amounts(result, "xy")
    assert x == Amount(10, U.r)
    assert y == Amount(5, U.s)


def test_unit_conversion():
    g = Unit("g")
    kg = Unit("kg", {g: lambda k: k * 1000.})
    assert g.to(g)(100) == 100
    assert kg.to(g)(1) == 1000
    assert Amount(1, kg) + Amount(1000, g) == Amount(2000, g)


def test_amounts_behave_as_monoid():
    assert growser.add_amount(Amount(5, U.r), Amount(10, U.r)) == Amount(15, U.r)
    assert growser.sum_amounts([Amount(5, U.r), Amount(10, U.r)]) == Amount(15, U.r)
    a = Amount(5, U.r)
    b = Amount(10, U.r)
    c = Amount(3, U.r)
    assert a + b == Amount(15, U.r)
    with(pytest.raises(ArithmeticError)):
        _ = a + Amount(10, U.t)
    assert a + Amount.zero == a
    assert Amount.zero + a == a
    assert (a + b) + c == a + (b + c)

    assert reduce(add, (a, b, a, b), Amount.zero) == Amount(30, U.r)

def ingredient(name, amount, unit):
    return growser.Ingredient(name, Amount(amount, unit))

x = ingredient("x", 1, U.r)
y = ingredient("y", 1, U.s)
z = ingredient("z", 1, U.t)

a = growser.IngredientList([x, y])
b = growser.IngredientList([x, z])
c = growser.IngredientList([y, z, Ingredient("q", Amount(1, Unit("#")))])

def test_ingredient_lists_behaves_as_a_monoid():

    assert a == a
    assert a + a.zero == a
    assert a.zero + a == a
    assert (a + b) + c == a + (b + c)

    assert a + b == growser.IngredientList([
        Ingredient("x", Amount(2, U.r)),
        y, z
    ])

def test_ingredient_lists_can_be_scaled():
    s = 2.0 * a
    x, y = extract_amounts(s, "xy")
    assert x == Amount(2, U.r)

def test_recipe_can_be_compound():
    compound = CompoundRecipe(for_people=4, recipes=[recipe, recipe2])
    ingredients = compound.ingredients
    x, y = extract_amounts(ingredients, "xy")
    assert x == Amount(8, U.r)
    assert y == Amount(8, U.s)

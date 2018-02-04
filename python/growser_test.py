"""tests for the growser script"""
from functools import reduce
from operator import add

import pytest

from entities import Recipe, Ingredient, Amount, Serving, Unit
import growser


class u:
    r = Unit("r")
    s = Unit("s")
    t = Unit("t")

recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, u.r))])


def test_recipe_amount_for_more_people():
    scaled = growser.serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2


def test_needed_ingredients_from_menu_are_accumulated():
    recipes = {
        "dish1": Recipe(1, [
            Ingredient("x", Amount(1, u.r)),
            Ingredient("y", Amount(1, u.s))]),
        "dish2": Recipe(1, [
            Ingredient("y", Amount(1, u.s)),
            Ingredient("z", Amount(1, u.t))])
    }
    servings = [
        Serving("dish1", 2),
        Serving("dish2", 3)
    ]
    ingredients = growser.needed_ingredients(servings, recipes)
    assert len(ingredients) == 3
    x, y, z = map(lambda n: next(i for i in ingredients if i.name == n).amount, "xyz")
    assert x == Amount(2, u.r)
    assert y == Amount(5, u.s)
    assert z == Amount(3, u.t)


def test_pantry_is_subtracted_from_need():
    need = [
        Ingredient("x", Amount(10, u.r)),
        Ingredient("y", Amount(10, u.s))
    ]
    assert len(growser.subtract_ingredients(need, need)) == 0
    assert growser.subtract_ingredients(need, []) == need
    result = growser.subtract_ingredients(need, [Ingredient("y", Amount(5, u.s))])
    def amount_for(name):
        return next(i for i in result if i.name == name).amount
    assert amount_for("x") == Amount(10, u.r)
    assert amount_for("y") == Amount(5, u.s)


def test_unit_conversion():
    g = Unit("g")
    kg = Unit("kg", {g: lambda kg: kg * 1000.})
    assert g.to(g)(100) == 100
    assert kg.to(g)(1) == 1000
    assert Amount(1, kg) + Amount(1000, g) == Amount(2000, g)


def test_amounts_behave_as_monoid():
    assert growser.add_amount(Amount(5, u.r), Amount(10, u.r)) == Amount(15, u.r)
    assert growser.sum_amounts([Amount(5, u.r), Amount(10, u.r)]) == Amount(15, u.r)
    a = Amount(5, u.r)
    b = Amount(10, u.r)
    c = Amount(3, u.r)
    assert a + b == Amount(15, u.r)
    with(pytest.raises(ArithmeticError)):
        a + Amount(10, u.t)
    assert a + Amount.zero == a
    assert Amount.zero + a == a
    assert (a + b) + c == a + (b + c)

    assert reduce(add, (a, b, a, b), Amount.zero) == Amount(30, u.r)


def test_ingredient_lists_behaves_as_a_monoid():
    x = growser.ingredient("x", 1, u.r)
    y = growser.ingredient("y", 1, u.s)
    z = growser.ingredient("z", 1, u.t)

    a = growser.IngredientList([x, y])
    b = growser.IngredientList([x, z])
    c = growser.IngredientList([y, z, Ingredient("q", Amount(1, Unit("#")))])

    assert a == a
    assert a + a.zero == a
    assert a.zero + a == a
    assert (a + b) + c == a + (b + c)

    assert a + b == growser.IngredientList([
        Ingredient("x", Amount(2, u.r)),
        y, z
    ])


"""tests for the growser script"""

from entities import Recipe, Ingredient, Amount, Serving
import growser

recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, "."))])

def test_amount_is_scaled():
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
"""tests for the growser script"""

from entities import Recipe, Ingredient, Amount, Serving
import growser

recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, "."))])

def test_amount_is_scaled():
    scaled = growser.serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2


def test_needed_ingredients_from_menu():
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

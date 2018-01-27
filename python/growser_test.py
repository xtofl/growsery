"""tests for the growser script"""

from entities import Recipe, Ingredient, Amount
from growser import serve_for


def test_amount_is_scaled():
    recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, "."))])
    scaled = serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2

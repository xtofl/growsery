#!/usr/bin/python
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
    "pasta bolognese": Recipe(for_people=5, ingredients=[
        Ingredient("pasta", Amount(1.5, "pak")),
        Ingredient("gehakt", Amount(500, "gram")),
        Ingredient("paprika", Amount(2, "stuks")),
        Ingredient("tomatenconcentraat", Amount(2, "blikjes")),
        Ingredient("ui", Amount(1, "stuk")),
        Ingredient("look", Amount(1, "teentje"))
    ] + basis_recipes["witte saus"]),
    "kip met currysaus, perziken en patatten": Recipe(for_people=5, ingredients=[]),
}

Serving = namedtuple("Serving", ["recipe_name", "for_people"])

menu = {
    "zaterdag": Serving(recipe_name="papaschotel", for_people=5),
    "zondag": Serving(recipe_name="salade met eitjes en ovenschotel met pasta en tomatensaus", for_people=7),
    "maandag": Serving(recipe_name="balletjes tomatensaus met boontjes", for_people=7),
    "dinsdag": Serving(recipe_name="pasta bolognese", for_people=7),
    "woensdag": Serving(recipe_name="kip met currysaus, perziken en patatten", for_people=7)
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


def needed_ingredients(servings, recipes):
    def serve(s):
        return serve_for(s.for_people, recipes[s.recipe_name])
    dishes = [serve(s) for s in servings]
    return [ingredient
        for dish in dishes
        for ingredient in dish.ingredients]


def resulting_list(menu, recipes, pantry):
    dishes = menu.values()
    ingredients_needed = needed_ingredients(menu.values(), recipes)
    results = [\
        subtract_pantry(i, pantry)\
        for i in ingredients_needed]
    return results

def serve_for(for_people, recipe):
    scale = for_people / float(recipe.for_people)
    def scale_ingredient(i):
        return Ingredient(i.name, Amount(i.amount.number * scale, i.amount.unit))
    return Recipe(for_people=for_people,
        ingredients=map(scale_ingredient, recipe.ingredients)
    )

def test_amount_is_scaled():
    recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, "."))])
    scaled = serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2

def print_ingredients(ingredients):
    for ingredient in ingredients:
        print("{0:<20}: {1:>6} {2}".format(
            ingredient.name,
            ingredient.amount.number,
            ingredient.amount.unit))

def main():
    print("needed ingredients")
    print_ingredients(needed_ingredients(menu.values(), recipes))
    shopping_list = resulting_list(menu, recipes, pantry)
    print("\nshopping list")
    print_ingredients(shopping_list)

if __name__ == "__main__":
    main()
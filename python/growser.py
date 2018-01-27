#!/usr/bin/python
from collections import namedtuple
import sys

Amount = namedtuple("Amount", ["number", "unit"])
Ingredient = namedtuple("Ingredient", ["name", "amount"])

basis_recipes = {
    "witte saus": [
        Ingredient("bloem", Amount(50, "gram")),
        Ingredient("bakboter", Amount(1, "beetje")),
        Ingredient("melk", Amount(.8, "liter")),        
    ],
    "puree": [
        Ingredient("patat", Amount(5*3, "stuk")),
        Ingredient("bakboter", Amount(1, "beetje")),
        Ingredient("nootmuskaat", Amount(1, "beetje")),
        Ingredient("ei", Amount(1, "stuk")),
    ]
}

Recipe = namedtuple("Recipe", ["for_people", "ingredients"])

recipes = {
    "groentensoep":
        Recipe(for_people=2, ingredients=[
            Ingredient("selder", Amount(.5, "stuk")),
            Ingredient("wortel", Amount(4, "stuk")),
            Ingredient("prei", Amount(2, "stelen")),
            Ingredient("ui", Amount(1, "stuk")),
            Ingredient("bouillon", Amount(1, "blokje"))
        ]),
    "papaschotel":
        Recipe(for_people=5, ingredients=[
            Ingredient("witte kool", Amount(.5, "stuk")),
            Ingredient("gehakt", Amount(500, "gram")),
            Ingredient("geraspte kaas", Amount(500, "gram")),
            ] + basis_recipes["puree"]),
    "salade met eitjes en ovenschotel met pasta en tomatensaus":
        Recipe(for_people=5, ingredients=[
            Ingredient("ijsbergsla", Amount(0.3, "krop")),
            Ingredient("ei", Amount(6, "stuk")),
            Ingredient("krulletjes", Amount(500, "gram")),
            Ingredient("tomatenconcentraat", Amount(2, "blikje")),
        ] + basis_recipes["witte saus"]),
    "balletjes tomatensaus met boontjes":
        Recipe(for_people=5, ingredients=[
            Ingredient("patatten", Amount(5*3, "stuk")),
            Ingredient("gehakt", Amount(500, "gram")),
            Ingredient("boontjes", Amount(2, "pakjes")),
            ] + basis_recipes["witte saus"] + [
            Ingredient("tomatenconcentraat", Amount(2, "blikje")),
        ]),
    "pasta bolognese": Recipe(for_people=5, ingredients=[
        Ingredient("pasta", Amount(1.5, "pak")),
        Ingredient("wortel", Amount(4, "stuk")),
        Ingredient("gehakt", Amount(500, "gram")),
        Ingredient("paprika", Amount(2, "stuk")),
        Ingredient("tomatenconcentraat", Amount(2, "blikje")),
        Ingredient("emmental", Amount(300, "gram")),
        Ingredient("ui", Amount(1, "stuk")),
        Ingredient("look", Amount(1, "teentje"))
    ] + basis_recipes["witte saus"]),
    "kip met currysaus, perziken en patatten": Recipe(for_people=5, ingredients=[
        Ingredient("kipfilet", Amount(500, "gram")),
        Ingredient("perziken in blik", Amount(1, "blikje")),
        Ingredient("currysaus", Amount(2, "zakjes")),
        Ingredient("patatten", Amount(5*2, "stuk")),
        Ingredient("melk", Amount(1, "liter"))
    ]),
}

Serving = namedtuple("Serving", ["recipe_name", "for_people"])

menu = [
    Serving(recipe_name="groentensoep", for_people=5),
    Serving(recipe_name="papaschotel", for_people=5),
    
    Serving(
        for_people=7,
        recipe_name="salade met eitjes en ovenschotel met pasta en tomatensaus",
        ),
    
    Serving(recipe_name="balletjes tomatensaus met boontjes", for_people=7),
    
    Serving(recipe_name="pasta bolognese", for_people=5),
    
    Serving(recipe_name="kip met currysaus, perziken en patatten", for_people=5)
]

pantry = [
    Ingredient("bouillon", Amount(8, "blokje")),

    Ingredient("witte kool", Amount(1, "stuk")),
    Ingredient("bakboter", Amount(2, "fles")),
    Ingredient("pasta", Amount(1, "pak")),
    Ingredient("krulletjes", Amount(500, "gram")),
    Ingredient("nootmuskaat", Amount(100, "beetje")),
    Ingredient("gehakt", Amount(500, "gram")),
    Ingredient("ei", Amount(11, "stuk")),
    Ingredient("bouillon", Amount(8, "blojke")),
    Ingredient("patat", Amount(20, "stuk")),
    Ingredient("perziken in blik", Amount(3, "blikje")),
    Ingredient("tomatenconcentraat", Amount(2, "blikje")),

    Ingredient("currysaus", Amount(3, "zakjes")),

    Ingredient("ijsbergsla", Amount(1, "krop")),

    Ingredient("ui", Amount(1, "stuk")),

    Ingredient("gehakt", Amount(300, "gram")),
    Ingredient("kipfilet", Amount(400, "gram")),
    Ingredient("chipolata", Amount(10, "stuk")),

    Ingredient("kroketten", Amount(1, "zak")),
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

def test_amount_is_scaled():
    recipe = Recipe(for_people=1, ingredients=[Ingredient("x", Amount(1, "."))])
    scaled = serve_for(2, recipe)
    assert scaled.ingredients[0].amount.number == 2

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
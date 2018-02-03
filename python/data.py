from entities import *


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

recipes = {
    "koekjes": Recipe(for_people=5, ingredients=[
        Ingredient("koekjes", Amount(10, "stuk")),
        Ingredient("yoghurtjes", Amount(3, "potje"))
        ]),

    "fruit": Recipe(for_people=5, ingredients=[Ingredient("fruit", Amount(10, "stuk"))]),

    "beleg": Recipe(for_people=1, ingredients=[
        Ingredient("kaas", Amount(1, "plakje")),
        Ingredient("choco", Amount(0.05, "pot")),
        Ingredient("papaboter", Amount(0.05, "bakje"))
    ]),

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


menu = [
    Serving(recipe_name="groentensoep", for_people=5),
    Serving(recipe_name="papaschotel", for_people=5),
    
    Serving(
        for_people=7,
        recipe_name="salade met eitjes en ovenschotel met pasta en tomatensaus",
        ),
    
    Serving(recipe_name="balletjes tomatensaus met boontjes", for_people=7),
    
    Serving(recipe_name="pasta bolognese", for_people=5),
    
    Serving(recipe_name="kip met currysaus, perziken en patatten", for_people=5),

] + [
    Serving(recipe_name="koekjes", for_people=3),
    Serving(recipe_name="fruit", for_people=5),
    Serving(recipe_name="beleg", for_people=5)] * 7


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
    Ingredient("patat", Amount(20+30, "stuk")),
    Ingredient("perziken in blik", Amount(3, "blikje")),
    Ingredient("tomatenconcentraat", Amount(2, "blikje")),

    Ingredient("currysaus", Amount(3, "zakjes")),
    Ingredient("choco", Amount(1.5, "pot")),

    Ingredient("ijsbergsla", Amount(1, "krop")),

    Ingredient("ui", Amount(1, "stuk")),

    Ingredient("gehakt", Amount(300, "gram")),
    Ingredient("kipfilet", Amount(400, "gram")),
    Ingredient("chipolata", Amount(10, "stuk")),

    Ingredient("kroketten", Amount(1, "zak")),

    Ingredient("fruit", Amount(10, "stuk")),
    Ingredient("koekjes", Amount(20, "stuk")),
]

extras = [
    Ingredient("afwasblokjes", Amount(1, "doos"))
]

conversions = {
    ("beetje", "fles"): lambda x: Amount(x.number / 100., "fles")
}
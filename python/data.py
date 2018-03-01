from entities import *
from units import *
from recipes import *
from pantry import pantry

menu = [
    Serving(Recipes.groentensoep, for_people=5),

    Serving(Recipes.pizza, for_people=5),
    Serving(Recipes.kip_met_currysaus_perziken_en_patatten, for_people=5),
    Serving(CompoundRecipe(5,
        [Recipes.kotelet, Recipes.patatten, Recipes.erwtjes_en_worteltjes]),
        for_people=5),
    Serving(Recipes.pasta_bolognese, for_people=5),
    Serving(CompoundRecipe(5, [
        Recipes.rodekool,
        Recipes.worst,
        Recipes.patatten,
        Recipes.appelmoes
    ]), for_people=5),
    Serving(Recipes.wraps, for_people=5),
    Serving(Recipes.pannenkoeken, for_people=5), #reserve
] + [
    Serving(Recipes.granola, for_people=1),
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    Serving(Recipes.senseo, for_people=2),
    Serving(Recipes.nespresso, for_people=2)
    ] * 7


extras = [
    Ingredient("sportdrank", Amount(6, fles))
]

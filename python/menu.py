from entities import *
from units import *
from recipes import *
from pantry import pantry, from_pantry

reserve = [
    for_people(5)(
        Recipes.pannenkoeken,
        Recipes.rodekool, Recipes.worst, Recipes.kroketten, Recipes.appelmoes,
        Recipes.pudding,
        )
]

menu = [
    Serving(Recipes.groentensoep, for_people=5),

    #zaterdag
    for_people(5).serve(
        Recipes.slaatje_gezond,
        Recipes.tiramisu),

    #zondag
    for_people(5).serve(
        Recipes.balletjes_tomatensaus_met_boontjes
    ),

    #maandag
    for_people(5).serve(
        Recipes.wraps,
        Recipes.pudding
    ),

    #dinsdag
    for_people(5).serve(
        Recipes.pasta_bolognese),

    #woensdag
    for_people(5).serve(
        Recipes.kip_met_currysaus_perziken_en_patatten
    ),

    #donderdag
    for_people(5).serve(
        Recipes.worst,
        Recipes.rodekool,
        Recipes.appelmoes
    ),

    #vrijdag
    for_people(5).serve(
        Recipes.vis,
        Recipes.erwtjes_en_worteltjes,
        Recipes.patatten
    )

] + [
    Serving(Recipes.granola, for_people=1),
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    Serving(Recipes.senseo, for_people=2),
    Serving(Recipes.nespresso, for_people=2)
    ] * 7 \
+ reserve


extras = [
    Ingredient("sportdrank", Amount(6, fles)),
]

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
    # for_people(5).serve(
    #     Recipes.slaatje_gezond,
    #     Recipes.friet
    # ),

    #maandag
    for_people(1).serve(
        Recipes.kip_met_currysaus_perziken_en_patatten,
    ),

    #dinsdag
    for_people(5).serve(
        Recipes.worst,
        Recipes.wortelpuree
    ),

    #woensdag
    for_people(5).serve(
        Recipes.wraps
    ),

    #donderdag
    for_people(5).serve(
        Recipes.pizza_oetker,
    ),

    #vrijdag
    for_people(4).serve(
        Recipes.pasta_bolognese),

    #zaterdag
    for_people(4).serve(
        Recipes.kippenboutjes
    )
]

all_dishes = menu + [
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    Serving(Recipes.senseo, for_people=2),
    Serving(Recipes.nespresso, for_people=2),
    ] * 7 \
    + [
        just("citroenthee", Amount(1, doos))
    ] \
+ reserve

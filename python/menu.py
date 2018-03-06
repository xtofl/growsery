from entities import *
from units import *
from recipes import *
from pantry import pantry, from_pantry

reserve = [
    for_people(5)(Recipes.pannenkoeken),
    for_people(5)(Recipes.rodekool, Recipes.worst, Recipes.kroketten, Recipes.appelmoes)
]

menu = [
    Serving(Recipes.groentensoep, for_people=5),

    #zaterdag
    for_people(2).serve(Recipes.scampi),
    for_people(3).serve(Recipes.vis),
    for_people(5).serve(Recipes.risotto),
    
    #zondag
    for_people(5).serve(
        Recipes.rodekool,
        Recipes.worst,
        Recipes.kroketten,
        Recipes.appelmoes
    ),

    #dinsdag
    for_people(5).serve(
        Recipes.pasta_bolognese),

    #woensdag
    for_people(5).serve(
        Recipes.kippenboutjes,
        Recipes.basmati,
        Recipes.groentenmix,
        Recipes.appelmoes),

    #donderdag
    for_people(5).serve(
        Recipes.macaroni_met_ham_kaas_en_broccoli
    ),

    #vrijdag
    for_people(5).serve(Recipes.friet)

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

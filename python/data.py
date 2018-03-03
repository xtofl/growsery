from entities import *
from units import *
from recipes import *
from pantry import pantry, from_pantry


menu = [
    Serving(Recipes.groentensoep, for_people=5),

    for_people(2).serve(Recipes.scampi),
    for_people(3).serve(Recipes.vis),
    for_people(5).serve(Recipes.risotto),
    
    for_people(5).serve(
        Recipes.rodekool,
        Recipes.worst,
        Recipes.kroketten,
        Recipes.appelmoes
    ),

    for_people(5).serve(
        Recipes.pasta_bolognese),

    for_people(5).serve(
        Recipes.kippenboutjes,
        Recipes.basmati,
        Recipes.groentenmix,
        Recipes.appelmoes),

    for_people(5).serve(
        Recipes.pasta_kaassaus_hamblokjes
    ),

] + [
    Serving(Recipes.granola, for_people=1),
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    Serving(Recipes.senseo, for_people=2),
    Serving(Recipes.nespresso, for_people=2)
    ] * 7


extras = [
    Ingredient("sportdrank", Amount(6, fles)),
]

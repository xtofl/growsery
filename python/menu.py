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
    for_people(3).serve(Recipes.hamburger),
    for_people(2).serve(Recipes.veggieburger),
    for_people(5).serve(
        Recipes.erwtjes_en_worteltjes,
        Recipes.patatten
    ),

    #zondag
    for_people(6).serve(
        Recipes.balletjes_tomatensaus_met_boontjes,
        Recipes.patatten,
        Recipes.tiramisu
    ),

    #maandag
    for_people(5).serve(
        Recipes.papaschotel,
        Recipes.pudding
    ),

    #dinsdag
    for_people(5).serve(
        Recipes.pasta_bolognese),

    #woensdag
    for_people(2).serve(Recipes.kotelet),
    for_people(3).serve(Recipes.biefstuk),
    for_people(5).serve(
        Recipes.erwtjes_en_worteltjes,
        Recipes.basmati
    ),

    #donderdag
    for_people(5).serve(
        Recipes.macaroni_met_ham_kaas_en_broccoli,
    ),

    #vrijdag
    for_people(5).serve(
        Recipes.quiche_met_zalm_en_broccoli
    ),

] + [
    Serving(Recipes.granola, for_people=1),
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    Serving(Recipes.senseo, for_people=2),
    Serving(Recipes.nespresso, for_people=2)
    ] * 7 \
+ reserve

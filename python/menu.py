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
        Recipes.zalm,
        Recipes.erwtjes_en_worteltjes,
        Recipes.puree
    ),

    #zondag
    for_people(5).serve(
        Recipes.falafel,
        Recipes.sla, Recipes.tomaat,
        Recipes.pitabroodjes
    ),

    #maandag
     for_people(7).serve(
         Recipes.papaschotel,
     ),

    #dinsdag
    for_people(5).serve(
        Recipes.pasta_bolognese
    ),

    #woensdag
    for_people(5).serve(
        Recipes.wraps
    ),

    #donderdag
    for_people(5).serve(
        Recipes.pasta,
        Recipes.pesto,
    ),

    #vrijdag
    #zaterdag
]


all_dishes = menu + [
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    ] * 7 \
    + [
        just("citroenthee", Amount(1, doos)),
        just("zakdoekjes", Amount(2, doos)),
        just("pompelmoes", Amount(1, stuk)),
        just("tippex", Amount(2, stuk))
    ] \
    + [
        just("senseo", Amount(4, stuk))
    ] * 7 \
+ reserve

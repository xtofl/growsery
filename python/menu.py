from entities import *
from units import *
from recipes import *
from pantry import pantry, from_pantry

reserve = [
    for_people(5)(
        Recipes.pannenkoeken,
        Recipes.rodekool, Recipes.worst, Recipes.kroketten, Recipes.appelmoes,
        Recipes.pudding,
        ),
    just("lactosevrije yoghurt", Amount(6, potje)),
    just("melk", Amount(3, liter)),
    just("paneermeel", Amount(1, doosje)),
    just("allesreiniger", Amount(1, fles)),
    just("keukenrol", Amount(6, stuk)),
    just("dweildoekjes", Amount(2, zak)),
    just("honing", Amount(1, pot)),
    just("rubber handschoentjes", Amount(1, doos)),
]

menu = [
    Serving(Recipes.groentensoep, for_people=5),

    #zaterdag
    for_people(5).serve(
        Recipes.wraps,
    ),

    #zondag
    for_people(5).serve(
        Recipes.falafel,
        Recipes.sla, Recipes.tomaat,
        Recipes.pitabroodjes
    ),

    #maandag
    for_people(5).serve(
        Recipes.papaschotel,
    ),

    #dinsdag
    for_people(5).serve(
        Recipes.pasta_bolognese
    ),

    #woensdag
    for_people(5).serve(
        Recipes.biefstuk,
        Recipes.kroketten,
        Recipes.zelfgemaakte_appelmoes
    ),

    #donderdag
    for_people(5).serve(
        Recipes.quiche_met_zalm_en_broccoli
    ),

    #vrijdag
    for_people(5).serve(
        Recipes.pasta_carbonara
    ),
    #zaterdag
]


all_dishes = menu + [
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    ] * 7 \
    + [
        just("ontstopper", Amount(1, stuk))
    ] \
+ reserve

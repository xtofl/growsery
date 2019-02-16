from entities import *
from units import *
from recipes import *

reserve = [
    for_people(5)(
        Recipes.pannenkoeken,
        Recipes.rodekool, Recipes.worst, Recipes.kroketten, Recipes.appelmoes,
        Recipes.pudding,
        ),
    just("lactosevrije yoghurt", Amount(6, potje)),
    just("melk", Amount(3, liter)),
    just("paneermeel", Amount(1, doosje)),
    just("keukenrol", Amount(6, stuk)),
    just("wc-papier", Amount(6, stuk)),
    just("dweildoekjes", Amount(2, zak)),
    just("honing", Amount(1, pot)),
    just("rubber handschoentjes", Amount(1, doos)),
    just("basmati", Amount(200, g)),
    just("zwarte chocola", Amount(500, g)),
]

menu = [
    Serving(Recipes.groentensoep, for_people=5),

    #zaterdag
    for_people(4).serve(
        Recipes.slaatje_gezond, Recipes.kroketten
    ),

    #zondag
    for_people(5).serve(
        Recipes.zalm,
    ),
]


all_dishes = menu + [
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    ] * 7 \
+ reserve

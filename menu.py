from itertools import starmap

from entities import Serving, for_people
from recipes import Recipes

reserve = (
    for_people(5)(
        Recipes.pannenkoeken,
        Recipes.witte_saus,

        Recipes.pudding,
        ),
)

for_five = for_people(5).serve

menu_a = tuple(starmap(for_five, (
    (Recipes.veggie_pasta("schelpjes"),),
    (Recipes.pizza,),
    (Recipes.zalm_ovenschotel,),
    (Recipes.volauvent,),
    (Recipes.pasta_bolognese,),
    (Recipes.witloof_zalm, Recipes.wortelpuree),
)))

menu_b = tuple(
)

menu = menu_a[:3] \
       + 3 * (
            Serving(Recipes.granola, for_people=1),
            Serving(Recipes.koekjes, for_people=3),
            Serving(Recipes.fruit, for_people=5),
            Serving(Recipes.beleg, for_people=5),
        ) \
        + reserve

from entities import *


basis_recipes = {
    "witte saus": [
        Ingredient("bloem", Amount(50, "gram")),
        Ingredient("bakboter", Amount(1, "beetje")),
        Ingredient("melk", Amount(.8, "liter")),        
    ],
    "puree": [
        Ingredient("patat", Amount(5*3, "stuk")),
        Ingredient("bakboter", Amount(1, "beetje")),
        Ingredient("nootmuskaat", Amount(1, "beetje")),
        Ingredient("ei", Amount(1, "stuk")),
    ]
}

recipes = {
    "koekjes": Recipe(for_people=5, ingredients=[
        Ingredient("koekjes", Amount(10, "stuk")),
        Ingredient("yoghurtjes", Amount(3, "potje"))
        ]),

    "fruit": Recipe(for_people=5, ingredients=[Ingredient("fruit", Amount(10, "stuk"))]),

    "beleg": Recipe(for_people=1, ingredients=[
        Ingredient("kaas", Amount(1, "plakje")),
        Ingredient("choco", Amount(0.05, "pot")),
        Ingredient("papaboter", Amount(0.02, "bakje"))
    ]),

    "groentensoep":
        Recipe(for_people=2, ingredients=[
            Ingredient("selder", Amount(.5, "stuk")),
            Ingredient("wortel", Amount(4, "stuk")),
            Ingredient("prei", Amount(2, "stelen")),
            Ingredient("ui", Amount(1, "stuk")),
            Ingredient("bouillon", Amount(1, "blokje"))
        ]),
    "papaschotel":
        Recipe(for_people=5, ingredients=[
            Ingredient("witte kool", Amount(.5, "stuk")),
            Ingredient("gehakt", Amount(500, "gram")),
            Ingredient("geraspte kaas", Amount(500, "gram")),
            ] + basis_recipes["puree"]),
    "salade met eitjes en ovenschotel met pasta en tomatensaus":
        Recipe(for_people=5, ingredients=[
            Ingredient("ijsbergsla", Amount(0.3, "krop")),
            Ingredient("ei", Amount(6, "stuk")),
            Ingredient("krulletjes", Amount(500, "gram")),
            Ingredient("tomatenconcentraat", Amount(2, "blikje")),
        ] + basis_recipes["witte saus"]),
    "balletjes tomatensaus met boontjes":
        Recipe(for_people=5, ingredients=[
            Ingredient("patatten", Amount(5*3, "stuk")),
            Ingredient("gehakt", Amount(500, "gram")),
            Ingredient("boontjes", Amount(2, "pakjes")),
            ] + basis_recipes["witte saus"] + [
            Ingredient("tomatenconcentraat", Amount(2, "blikje")),
        ]),
    "pasta bolognese": Recipe(for_people=5, ingredients=[
        Ingredient("pasta", Amount(1.5, "pak")),
        Ingredient("wortel", Amount(4, "stuk")),
        Ingredient("gehakt", Amount(300, "gram")),
        Ingredient("paprika", Amount(2, "stuk")),
        Ingredient("tomatenconcentraat", Amount(2, "blikje")),
        Ingredient("emmental", Amount(300, "gram")),
        Ingredient("ui", Amount(1, "stuk")),
        Ingredient("look", Amount(1, "teentje"))
    ] + basis_recipes["witte saus"]),
    "kip met currysaus, perziken en patatten": Recipe(for_people=5, ingredients=[
        Ingredient("kipfilet", Amount(500, "gram")),
        Ingredient("perziken in blik", Amount(1, "blikje")),
        Ingredient("currysaus", Amount(2, "zakjes")),
        Ingredient("patatten", Amount(5*2, "stuk")),
        Ingredient("melk", Amount(1, "liter"))
    ]),
    "cordon bleu": Recipe(for_people=5, ingredients=[
        Ingredient("cordon bleu", Amount(5, "stuk"))
    ]),
    "wortelpuree": Recipe(for_people=5, ingredients=[
        Ingredient("patatten", Amount(5*3, "stuk")),
        Ingredient("wortel", Amount(5*2, "stuk")),
        Ingredient("ei", Amount(1, "stuk")),
        Ingredient("melk", Amount(0.5, "liter")),
        Ingredient("nootmuskaat", Amount(1, "beetje"))
    ]),
    "aardappels in witte saus": Recipe(for_people=5, ingredients=[
        Ingredient("patatten", Amount(5*2, "stuk")),
        Ingredient("bloem", Amount(100, "gram")),
        Ingredient("bakboter", Amount(3, "beetje")),
        Ingredient("geraspte kaas", Amount(1, "zakje"))
    ]),
    "erwtjes en worteltjes": Recipe(for_people=5, ingredients=[
        Ingredient("diepvrieserwten", Amount(0.5, "kg")),
        Ingredient("wortel", Amount(8, "stuk"))
    ]),
    "witte kool": Recipe(for_people=5, ingredients=[
        Ingredient("witte kool", Amount(0.5, "stuk")),
    ]),
    "kotelet": Recipe(for_people=5, ingredients=[
        Ingredient("kotelet", Amount(5, "stuk")),
        Ingredient("bakboter", Amount(1, "beetje"))
    ]),
    "kaassaus": Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(100, "gram")),
        Ingredient("bakboter", Amount(3, "beetje")),
        Ingredient("geraspte kaas", Amount(1, "zakje")),
        Ingredient("melk", Amount(1, "liter"))
    ]),
    "quiche met zalm en broccoli": Recipe(for_people=5, ingredients=[
        Ingredient("kruimeldeeg", Amount(1, "stuk")),
        Ingredient("ei", Amount(4, "stuk")),
        Ingredient("melk", Amount(.25, "liter")),
        Ingredient("diepvries broccoli", Amount(.5, "zak")),
        Ingredient("geraspte kaas", Amount(1, "zakje")),
        Ingredient("gerookte zalm", Amount(1, "pak")),
    ]),
    "risotto": Recipe(for_people=5, ingredients=[
        Ingredient("ui", Amount(1, "stuk")),
        Ingredient("bakboter", Amount(1, "beetje")),
        Ingredient("risotto", Amount(200, "gram"))
    ]),
    "macaroni met ham, kaas en broccoli": Recipe(for_people=5, ingredients=[
        Ingredient("krulletjes", Amount(300, "gram")),
        Ingredient("hamblokjes", Amount(150*5, "gram")),
        #kaassaus
        Ingredient("bloem", Amount(100, "gram")),
        Ingredient("bakboter", Amount(3, "beetje")),
        Ingredient("geraspte kaas", Amount(1, "zakje")),
        Ingredient("melk", Amount(1, "liter")),
        Ingredient("ketchup", Amount(0.3, "fles")),
    ]),
    "biefstuk": Recipe(for_people=5, ingredients=[
        Ingredient("biefstuk", Amount(4, "stuk")),
        Ingredient("bakboter", Amount(1, "beetje")),
    ]),
    "senseo": Recipe(for_people=2, ingredients=[Ingredient("senseo", Amount(2, "pad"))]),
    "nespresso": Recipe(for_people=1, ingredients=[Ingredient("nespresso", Amount(1, "capsule"))])
}


menu = [
    Serving(recipe_name="groentensoep", for_people=5),

    Serving(recipe_name="cordon bleu", for_people=5),
    Serving(recipe_name="wortelpuree", for_people=5),

    Serving(recipe_name="aardappels in witte saus", for_people=5),
    Serving(recipe_name="erwtjes en worteltjes", for_people=5),
    Serving("biefstuk", for_people=5),

    Serving(recipe_name="witte kool", for_people=5),
    Serving("kaassaus", 5),
    Serving(recipe_name="kotelet", for_people=5),

    Serving(recipe_name="pasta bolognese", for_people=5),

    Serving("quiche met zalm en broccoli", for_people=5),
    Serving("risotto", for_people=5),

    Serving("macaroni met ham, kaas en broccoli", for_people=5),

] + [
    Serving(recipe_name="koekjes", for_people=3),
    Serving(recipe_name="fruit", for_people=5),
    Serving(recipe_name="beleg", for_people=5),
    Serving(recipe_name="senseo", for_people=2),
    Serving(recipe_name="nespresso", for_people=2)
    ] * 7


pantry = [
    Ingredient("bouillon", Amount(8, "blokje")),
    Ingredient("citroenthee", Amount(0, "doosje")),
    Ingredient("senseo", Amount(10, "pad")),
    Ingredient("nespresso", Amount(40, "capsule")),

    Ingredient("patat", Amount(20, "stuk")),

    Ingredient("currysaus", Amount(1, "zakje")),

    Ingredient("nootmuskaat", Amount(100, "beetje")),

    #frigo
    Ingredient("witte kool", Amount(.5, "stuk")),
    Ingredient("bakboter", Amount(.1, "fles")),
    Ingredient("ei", Amount(0, "stuk")),
    Ingredient("ketchup", Amount(0, "fles")),

    Ingredient("risotto", Amount(1.5, "kg")),
    Ingredient("basmati", Amount(1.2, "kg")),

    Ingredient("bloem", Amount(3, "kg")),
    Ingredient("pasta", Amount(3, "pak")),
    Ingredient("krulletjes", Amount(500, "gram")),

    Ingredient("perziken in blik", Amount(1, "blikje")),
    Ingredient("tomatenconcentraat", Amount(3, "blikje")),
    Ingredient("yoghurtjes", Amount(6, "potje")),

    Ingredient("choco", Amount(1, "pot")),

    Ingredient("ijsbergsla", Amount(1, "krop")),

    Ingredient("ui", Amount(0, "stuk")),

    Ingredient("gehakt", Amount(300, "gram")),
    Ingredient("kipfilet", Amount(0, "gram")),
    Ingredient("chipolata", Amount(0, "stuk")),
    Ingredient("kippenbout", Amount(4, "stuk")),
    Ingredient("kalkoenschnitzel", Amount(4, "stuk")),

    Ingredient("kroketten", Amount(1, "zak")),

    Ingredient("diepvries broccoli", Amount(1, "zak")),
    Ingredient("diepvrieserwten", Amount(1, "kg")),

    Ingredient("fruit", Amount(2, "stuk")),
    Ingredient("koekjes", Amount(20, "stuk")),
]

extras = [
    Ingredient("afwasblokjes", Amount(1, "doos")),
]

conversions = {
    ("beetje", "fles"): lambda x: Amount(x.number / 100., "fles"),
    ("gram", "kg"): lambda x: Amount(x.number / 1000, "kg"),
}
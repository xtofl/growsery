from entities import *


#units
gram = Unit("g")
kg = Unit("kg", {gram: lambda kg: kg/1000.})

beetje = Unit("beetje")
fles = Unit("fles", {beetje: lambda x: x/1000.})

stuk = Unit("stuk")

liter = Unit("liter")

potje = Unit("potje")
plakje = Unit("plakje")
pot = Unit("pot")
bakje = Unit("bakje")
blik = Unit("blik")
blikje = Unit("blikje")
zakje = Unit("zakje")
teentje = Unit("teentje")

zak = Unit("zak")
pak = Unit("pak")

senseo_pad = Unit("pad")
koffie_capsule = Unit("capsule")
doosje = Unit("doosje")
doos = Unit("doos")

class BasicRecipes:
    puree = Recipe(for_people=5, ingredients=[
        Ingredient("patat", Amount(5*3, stuk)),
        Ingredient("bakboter", Amount(1, beetje)),
        Ingredient("nootmuskaat", Amount(1, beetje)),
        Ingredient("ei", Amount(1, stuk)),
    ])
    papakool = Recipe(for_people=5, ingredients=[
        Ingredient("witte kool", Amount(.5, stuk)),
        Ingredient("gehakt", Amount(500, gram)),
        Ingredient("geraspte kaas", Amount(500, gram)),
    ])
    witte_saus = Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(50, gram)),
        Ingredient("bakboter", Amount(1, beetje)),
        Ingredient("melk", Amount(.8, liter)),
    ])
    tomatensaus = Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(50, gram)),
        Ingredient("bakboter", Amount(1, beetje)),
        Ingredient("melk", Amount(.8, liter)),
        Ingredient("tomatenconcentraat", Amount(2, blik))
    ])

    koekjes = Recipe(for_people=5, ingredients=[
        Ingredient("koekjes", Amount(10, stuk)),
        Ingredient("yoghurtjes", Amount(3, potje))
        ])

    fruit = Recipe(for_people=5, ingredients=[Ingredient("fruit", Amount(10, stuk))])

    beleg = Recipe(for_people=1, ingredients=[
        Ingredient("kaas", Amount(1, plakje)),
        Ingredient("choco", Amount(0.05, pot)),
        Ingredient("papaboter", Amount(0.02, bakje))
    ])

    groentensoep = Recipe(for_people=2, ingredients=[
            Ingredient("selder", Amount(.5, stuk)),
            Ingredient("wortel", Amount(4, stuk)),
            Ingredient("prei", Amount(2, stuk)),
            Ingredient("ui", Amount(1, stuk)),
            Ingredient("bouillon", Amount(1, stuk))
        ])

class Recipes(BasicRecipes):
    papaschotel = CompoundRecipe(for_people=5, recipes=[BasicRecipes.papakool, BasicRecipes.puree])
    salade_met_eitjes_en_ovenschotel_met_pasta_en_tomatensaus =\
        CompoundRecipe(for_people=5, recipes=[Recipe(for_people=5, ingredients=[
            Ingredient("ijsbergsla", Amount(0.3, stuk)),
            Ingredient("ei", Amount(6, stuk)),
            Ingredient("krulletjes", Amount(500, gram)),
        ]), BasicRecipes.tomatensaus])
    balletjes_tomatensaus_met_boontjes =\
        CompoundRecipe(5, [
            Recipe(for_people=5, ingredients=[
                Ingredient("patatten", Amount(5*3, stuk)),
                Ingredient("gehakt", Amount(500, gram)),
                Ingredient("boontjes", Amount(2, zakje)),
            ]),
            BasicRecipes.tomatensaus])
    pasta_bolognese = CompoundRecipe(5, [
        Recipe(for_people=5, ingredients=[
            Ingredient("pasta", Amount(1.5, pak)),
            Ingredient("wortel", Amount(4, stuk)),
            Ingredient("gehakt", Amount(300, gram)),
            Ingredient("paprika", Amount(2, stuk)),
            Ingredient("emmental", Amount(300, gram)),
            Ingredient("ui", Amount(1, stuk)),
            Ingredient("look", Amount(1, teentje))
        ]),
        BasicRecipes.tomatensaus])
    kip_met_currysaus_perziken_en_patatten = Recipe(for_people=5, ingredients=[
        Ingredient("kipfilet", Amount(500, gram)),
        Ingredient("perziken in blik", Amount(1, blik)),
        Ingredient("currysaus", Amount(2, zakje)),
        Ingredient("patatten", Amount(5*2, stuk)),
        Ingredient("melk", Amount(1, liter))
    ])
    cordon_bleu = Recipe(for_people=5, ingredients=[
        Ingredient("cordon bleu", Amount(5, stuk))
    ])
    wortelpuree = Recipe(for_people=5, ingredients=[
        Ingredient("patatten", Amount(5*3, stuk)),
        Ingredient("wortel", Amount(5*2, stuk)),
        Ingredient("ei", Amount(1, stuk)),
        Ingredient("melk", Amount(0.5, liter)),
        Ingredient("nootmuskaat", Amount(1, beetje))
    ])
    aardappels_in_witte_saus = Recipe(for_people=5, ingredients=[
        Ingredient("patatten", Amount(5*2, stuk)),
        Ingredient("bloem", Amount(100, gram)),
        Ingredient("bakboter", Amount(3, beetje)),
        Ingredient("geraspte kaas", Amount(1, zakje)),
        Ingredient("melk", Amount(1.5, liter))
    ])
    erwtjes_en_worteltjes = Recipe(for_people=5, ingredients=[
        Ingredient("diepvrieserwten", Amount(0.5, kg)),
        Ingredient("wortel", Amount(8, stuk))
    ])
    witte_kool = Recipe(for_people=5, ingredients=[
        Ingredient("witte kool", Amount(0.5, stuk)),
    ])
    kotelet = Recipe(for_people=5, ingredients=[
        Ingredient("kotelet", Amount(5, stuk)),
        Ingredient("bakboter", Amount(1, beetje))
    ])
    kaassaus = Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(100, gram)),
        Ingredient("bakboter", Amount(3, beetje)),
        Ingredient("geraspte kaas", Amount(1, zakje)),
        Ingredient("melk", Amount(1, liter))
    ])
    quiche_met_zalm_en_broccoli = Recipe(for_people=5, ingredients=[
        Ingredient("kruimeldeeg", Amount(1, stuk)),
        Ingredient("ei", Amount(4, stuk)),
        Ingredient("melk", Amount(.25, liter)),
        Ingredient("diepvries broccoli", Amount(.5, zak)),
        Ingredient("geraspte kaas", Amount(1, zakje)),
        Ingredient("gerookte zalm", Amount(1, pak)),
    ])
    risotto = Recipe(for_people=5, ingredients=[
        Ingredient("ui", Amount(1, stuk)),
        Ingredient("bakboter", Amount(1, beetje)),
        Ingredient("risotto", Amount(200, gram))
    ])
    macaroni_met_ham_kaas_en_broccoli = Recipe(for_people=5, ingredients=[
        Ingredient("krulletjes", Amount(300, gram)),
        Ingredient("hamblokjes", Amount(150*5, gram)),
        #kaassaus
        Ingredient("bloem", Amount(100, gram)),
        Ingredient("bakboter", Amount(3, beetje)),
        Ingredient("geraspte kaas", Amount(1, zakje)),
        Ingredient("melk", Amount(1, liter)),
        Ingredient("ketchup", Amount(0.3, fles)),
    ])
    biefstuk = Recipe(for_people=5, ingredients=[
        Ingredient("biefstuk", Amount(4, stuk)),
        Ingredient("bakboter", Amount(1, beetje)),
    ])
    senseo = Recipe(for_people=2, ingredients=[
        Ingredient("senseo", Amount(2, senseo_pad))])
    nespresso = Recipe(for_people=1, ingredients=[
        Ingredient("nespresso", Amount(1, koffie_capsule))])

menu = [
    Serving(Recipes.groentensoep, for_people=5),

    Serving(Recipes.cordon_bleu, for_people=5),
    Serving(Recipes.wortelpuree, for_people=5),

    Serving(Recipes.aardappels_in_witte_saus, for_people=5),
    Serving(Recipes.erwtjes_en_worteltjes, for_people=5),
    Serving(Recipes.biefstuk, for_people=5),

    Serving(Recipes.witte_kool, for_people=5),
    Serving(Recipes.kaassaus, 5),
    Serving(Recipes.kotelet, for_people=5),

    Serving(Recipes.pasta_bolognese, for_people=5),

    Serving(Recipes.quiche_met_zalm_en_broccoli, for_people=5),
    Serving(Recipes.risotto, for_people=5),

    Serving(Recipes.macaroni_met_ham_kaas_en_broccoli, for_people=5),

] + [
    Serving(Recipes.koekjes, for_people=3),
    Serving(Recipes.fruit, for_people=5),
    Serving(Recipes.beleg, for_people=5),
    Serving(Recipes.senseo, for_people=2),
    Serving(Recipes.nespresso, for_people=2)
    ] * 7


pantry = [
    Ingredient("bouillon", Amount(8, stuk)),
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(10, senseo_pad)),
    Ingredient("nespresso", Amount(40, koffie_capsule)),

    Ingredient("patat", Amount(20, stuk)),

    Ingredient("currysaus", Amount(1, zakje)),

    Ingredient("nootmuskaat", Amount(100, beetje)),

    #frigo
    Ingredient("witte kool", Amount(.5, stuk)),
    Ingredient("bakboter", Amount(.1, fles)),
    Ingredient("ei", Amount(0, stuk)),
    Ingredient("ketchup", Amount(0, fles)),

    Ingredient("risotto", Amount(1.5, kg)),
    Ingredient("basmati", Amount(1.2, kg)),

    Ingredient("bloem", Amount(3, kg)),
    Ingredient("pasta", Amount(3, pak)),
    Ingredient("krulletjes", Amount(500, gram)),

    Ingredient("perziken in blik", Amount(1, blik)),
    Ingredient("tomatenconcentraat", Amount(3, blik)),
    Ingredient("yoghurtjes", Amount(6, potje)),

    Ingredient("choco", Amount(1, pot)),

    Ingredient("ijsbergsla", Amount(1, stuk)),

    Ingredient("ui", Amount(0, stuk)),

    Ingredient("gehakt", Amount(300, gram)),
    Ingredient("kipfilet", Amount(0, gram)),
    Ingredient("chipolata", Amount(0, stuk)),
    Ingredient("kippenbout", Amount(4, stuk)),
    Ingredient("kalkoenschnitzel", Amount(4, stuk)),

    Ingredient("kroketten", Amount(1, zak)),

    Ingredient("diepvries broccoli", Amount(1, zak)),
    Ingredient("diepvrieserwten", Amount(1, kg)),

    Ingredient("fruit", Amount(2, stuk)),
    Ingredient("koekjes", Amount(20, stuk)),
]

extras = [
    Ingredient("afwasblokjes", Amount(1, doos)),
]

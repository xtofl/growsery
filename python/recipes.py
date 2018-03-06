from entities import *
from units import *

class BasicRecipes:
    puree = Recipe(for_people=5, ingredients=[
        Ingredient("patat", Amount(5*3, stuk)),
        Ingredient("bakboter", Amount(1, beetje)),
        Ingredient("nootmuskaat", Amount(1, beetje)),
        Ingredient("ei", Amount(1, stuk)),
    ])
    patatten = Recipe(for_people=5, ingredients=[
        Ingredient("patat", Amount(5*3, stuk))
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
        Ingredient("bakboter", Amount(.1, fles)),
        Ingredient("melk", Amount(.8, liter)),
        Ingredient("tomatenconcentraat", Amount(2, blik))
    ])
    worst = Recipe(for_people=5, ingredients=[
        Ingredient("chipolata", Amount(10, stuk))
    ])
    rodekool = Recipe(for_people=5, ingredients=[
        Ingredient("rode kool", Amount(1, pot))
    ])
    zelfgemaakte_appelmoes = Recipe(for_people=5, ingredients=[
        Ingredient("stoofappel", Amount(5, stuk))
    ])
    appelmoes = Recipe(for_people=7, ingredients=[
        Ingredient("appelmoes", Amount(1, pot))
    ])
    friet = Recipe(for_people=5, ingredients=[
        Ingredient("mayo", Amount(0.4, fles)),
    ])

    koekjes = Recipe(for_people=5, ingredients=[
        Ingredient("koekjes", Amount(10, stuk)),
        Ingredient("yoghurtjes", Amount(3, potje))
        ])

    fruit = Recipe(for_people=5, ingredients=[Ingredient("fruit", Amount(10, stuk))])

    beleg = Recipe(for_people=1, ingredients=[
        Ingredient("leerdammer", Amount(1, plakje)),
        Ingredient("choco", Amount(0.05, pot)),
        Ingredient("papaboter", Amount(0.02, bakje)),
        Ingredient("confituur", Amount(0.05, pot))
    ])

    groentensoep = Recipe(for_people=2, ingredients=[
            Ingredient("selder", Amount(.5, stuk)),
            Ingredient("wortel", Amount(4, stuk)),
            Ingredient("prei", Amount(2, stuk)),
            Ingredient("ui", Amount(1, stuk)),
            Ingredient("bouillon", Amount(1, stuk))
        ])
    pizzadeeg = Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(1, kg)),
        Ingredient("olijfolie", Amount(.2, liter)),
        Ingredient("ei", Amount(1, stuk)),
    ])
    pannenkoeken = Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(0.5, kg)),
        Ingredient("melk", Amount(1, liter)),
        Ingredient("ei", Amount(4, stuk)),
        Ingredient("vannillesuiker", Amount(1, zakje)),

        Ingredient("kinnekessuiker", Amount(20, gram)),
        Ingredient("leerdammer", Amount(2, plakje)),
        Ingredient("bloemsuiker", Amount(20, gram)),
        Ingredient("confituur", Amount(0.1, pot))
    ])
    granola = Recipe(for_people=1, ingredients=[
        Ingredient("granola", Amount(0.1, zak)),
        Ingredient("melk", Amount(0.3, liter))
    ])
    kaassaus = Recipe(for_people=5, ingredients=[
        Ingredient("bloem", Amount(100, gram)),
        Ingredient("bakboter", Amount(3, beetje)),
        Ingredient("geraspte kaas", Amount(1, zakje)),
        Ingredient("melk", Amount(1, liter))
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
                Ingredient("patat", Amount(5*3, stuk)),
                Ingredient("gehakt", Amount(500, gram)),
                Ingredient("boontjes", Amount(2, zakje)),
            ]),
            BasicRecipes.tomatensaus])
    pasta_bolognese = CompoundRecipe(5, [
        Recipe(for_people=5, ingredients=[
            Ingredient("pasta", Amount(300, gram)),
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
        Ingredient("patat", Amount(5*2, stuk)),
        Ingredient("melk", Amount(1, liter))
    ])
    cordon_bleu = Recipe(for_people=5, ingredients=[
        Ingredient("cordon bleu", Amount(5, stuk))
    ])
    wortelpuree = Recipe(for_people=5, ingredients=[
        Ingredient("patat", Amount(5*3, stuk)),
        Ingredient("wortel", Amount(5*2, stuk)),
        Ingredient("ei", Amount(1, stuk)),
        Ingredient("melk", Amount(0.5, liter)),
        Ingredient("nootmuskaat", Amount(1, beetje))
    ])
    aardappels_in_witte_saus = Recipe(for_people=5, ingredients=[
        Ingredient("patat", Amount(5*2, stuk)),
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
    macaroni_met_ham_kaas_en_broccoli = CompoundRecipe(
        for_people=5,
        recipes=[Recipe(for_people=5, ingredients=[
        Ingredient("krulletjes", Amount(300, gram)),
        Ingredient("hamblokjes", Amount(1, doosje)),
        Ingredient("ketchup", Amount(0.3, fles))
    ]),  BasicRecipes.kaassaus])

    biefstuk = Recipe(for_people=5, ingredients=[
        Ingredient("biefstuk", Amount(4, stuk)),
        Ingredient("bakboter", Amount(1, beetje)),
    ])
    groentenmix = Recipe(for_people=5, ingredients=[
        Ingredient("paprika", Amount(1, stuk)),
        Ingredient("ui", Amount(1, stuk)),
        Ingredient("diepvries broccoli", Amount(0.3, zak))
    ])
    basmati = Recipe(for_people=5, ingredients=[
        Ingredient("basmati", Amount(.1, kg))
    ])

    kippenboutjes = Recipe(for_people=5, ingredients=[
        Ingredient("kippenbout", Amount(7, stuk))
    ])

    vis = Recipe(for_people=1, ingredients=[
        Ingredient("vis", Amount(1, stuk))
    ])

    scampi = Recipe(for_people=2, ingredients=[
        Ingredient("scampi", Amount(1, zak)),
        Ingredient("look", Amount(1, teentje)),
        Ingredient("room", Amount(.3, fles))
    ])

    kroketten = Recipe(for_people=1, ingredients=[
        Ingredient("kroketten", Amount(7, stuk)),
        Ingredient("mayo", Amount(1./15, fles))])

    pizza = CompoundRecipe(for_people=5, recipes=[
        BasicRecipes.pizzadeeg,
        Recipe(for_people=5, ingredients=[
            Ingredient("tomatenconcentraat", Amount(2, blikje)),
            Ingredient("geraspte kaas", Amount(3, zakje)),
            Ingredient("hamblokjes", Amount(1, doosje)),
            Ingredient("olijfolie", Amount(0.25, liter)),
            Ingredient("spaghettikruiden", Amount(1, beetje)),
            Ingredient("paprika", Amount(1, stuk)),
            Ingredient("olijfjes", Amount(0.5, doosje)),
            Ingredient("ananas", Amount(1, blikje))
        ])
    ])
    wraps = Recipe(for_people=5, ingredients=[
        Ingredient("wraps", Amount(10, stuk)),
        Ingredient("komkommer", Amount(1, stuk)),
        Ingredient("look", Amount(1, teentje)),
        Ingredient("peper", Amount(1, beetje)),
        Ingredient("mais", Amount(1, blik)),
        Ingredient("ui", Amount(1, stuk)),
        Ingredient("kipfilet", Amount(300, gram)),
        Ingredient("kippenkruiden", Amount(1, beetje)),
        Ingredient("yoghurt", Amount(0.3, pot)),
        Ingredient("wortel", Amount(4, stuk)),
        Ingredient("ijsbergsla", Amount(.5, stuk))
    ])
    senseo = Recipe(for_people=2, ingredients=[
        Ingredient("senseo", Amount(2, senseo_pad))])
    nespresso = Recipe(for_people=1, ingredients=[
        Ingredient("nespresso", Amount(1, koffie_capsule))])


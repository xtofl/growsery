from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("prei", Amount(0, stuk)),
    Ingredient("chocola", Amount(5*200, gram)),

    Ingredient("bouillon", Amount(1, stuk)),
    Ingredient("groentenbouillon", Amount(8, stuk)),

    Ingredient("patat", Amount(20, stuk)),

    Ingredient("nootmuskaat", Amount(1, potje)),

    Ingredient("selder", Amount(0, stuk)),
    Ingredient("puddingpoeder", Amount(3, zakje)),
    Ingredient("currysaus", Amount(3, zakje)),
    Ingredient("kinnekessuiker", Amount(1.8, kg)),
    Ingredient("bloemsuiker", Amount(200, gram)),

    #frigo
    Ingredient("witte kool", Amount(0, stuk)),
    Ingredient("bakboter", Amount(2, fles)),
    Ingredient("ei", Amount(3, stuk)),

    Ingredient("leerdammer", Amount(0, plakje)),
    Ingredient("wortel", Amount(28, stuk)),
    Ingredient("witloof", Amount(4, stuk)),
    Ingredient("ijsbergsla", Amount(0, stuk)),
    Ingredient("hamblokjes", Amount(0, doosje)),
    Ingredient("salami", Amount(1, pak)),

    #kast
    Ingredient("vanillesuiker", Amount(4, zakje)),
    Ingredient("risotto", Amount(.5, kg)),
    Ingredient("basmati", Amount(.8, kg)),

    Ingredient("spaghettikruiden", Amount(2, potje)),
    Ingredient("kaneel", Amount(1, potje)),
    Ingredient("honing", Amount(1, pot)),

    Ingredient("bloem", Amount(1, kg)),
    Ingredient("pasta", Amount(700,gram)),
    Ingredient("krulletjes", Amount(500, gram)),
    Ingredient("schelpjes", Amount(0, gram)),

    Ingredient("fruit", Amount(15, stuk)),
    Ingredient("banaan", Amount(0, stuk)),
    Ingredient("appel", Amount(5, stuk)),
    Ingredient("druiven", Amount(0, doos)),
    Ingredient("persappelsienen", Amount(15, stuk)),

    Ingredient("perziken in blik", Amount(1, blik)),
    Ingredient("tomatenconcentraat", Amount(1, blik)),
    Ingredient("yoghurtjes", Amount(0, potje)),

    Ingredient("kwatta", Amount(1, pot)),
    Ingredient("nutella", Amount(1, pot)),

    Ingredient("ui", Amount(2, stuk)),
    Ingredient("look", Amount(10, teentje)),

    Ingredient("olijfolie", Amount(1, liter)),

    # diepvries
    Ingredient("kroketten", Amount(2.5, zak)),

    Ingredient("diepvries broccoli", Amount(1.3, zak)),
    Ingredient("diepvrieserwten", Amount(.5, kg)),

    Ingredient("gehakt", Amount(500, gram)),
    Ingredient("kipfilet", Amount(0, gram)),
    Ingredient("chipolata", Amount(4, stuk)),
    Ingredient("kalkoenschnitzel", Amount(0, stuk)),
    Ingredient("kotelet", Amount(0, stuk)),
    Ingredient("biefstuk", Amount(0, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),
    Ingredient("notenburger", Amount(0, stuk)),

    Ingredient("koekjes", Amount(0, stuk)),
    Ingredient("granola", Amount(0, zak)),

    Ingredient("melk", Amount(8, liter)),
    Ingredient("papaboter", Amount(1.3, bakje)),

    Ingredient("tomaten passata", Amount(2, doos)),
    Ingredient("mais", Amount(3, blik)),
    Ingredient("zwanworstjes", Amount(0, blik)),
    Ingredient("appelmoes", Amount(1, pot)),
    Ingredient("rode kool", Amount(2, pot)),
    Ingredient("wraps", Amount(6, stuk)),
    Ingredient("confituur", Amount(1, pot)),

    Ingredient("mayo", Amount(0, fles)),
    Ingredient("ketchup", Amount(1, fles)),
]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None

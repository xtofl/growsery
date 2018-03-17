from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("bouillon", Amount(14*4, stuk)),
    Ingredient("groentenbouillon", Amount(36, stuk)),
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(30, senseo_pad)),
    Ingredient("nespresso", Amount(9, koffie_capsule)),

    Ingredient("patat", Amount(30, stuk)),

    Ingredient("currysaus", Amount(3, zakje)),

    Ingredient("nootmuskaat", Amount(30, beetje)),
    Ingredient("kinnekessuiker", Amount(1.8, kg)),
    Ingredient("bloemsuiker", Amount(0, gram)),

    #frigo
    Ingredient("witte kool", Amount(.0, stuk)),
    Ingredient("bakboter", Amount(1, fles)),
    Ingredient("ei", Amount(8, stuk)),

    Ingredient("leerdammer", Amount(15, plakje)),
    Ingredient("wortel", Amount(15, stuk)),
    Ingredient("witloof", Amount(0, stuk)),
    Ingredient("ijsbergsla", Amount(0, stuk)),

    #kast
    Ingredient("risotto", Amount(.1, kg)),
    Ingredient("basmati", Amount(.1, kg)),

    Ingredient("bloem", Amount(.5, kg)),
    Ingredient("pasta", Amount(500,gram)),
    Ingredient("krulletjes", Amount(2000, gram)),

    Ingredient("perziken in blik", Amount(0, blik)),
    Ingredient("tomatenconcentraat", Amount(3, blik)),
    Ingredient("yoghurtjes", Amount(0, potje)),

    Ingredient("choco", Amount(2, pot)),

    Ingredient("ui", Amount(4, stuk)),

    # diepvries
    Ingredient("kroketten", Amount(0.8, zak)),

    Ingredient("diepvries broccoli", Amount(.6, zak)),
    Ingredient("diepvrieserwten", Amount(.1, kg)),

    Ingredient("gehakt", Amount(400, gram)),
    Ingredient("kipfilet", Amount(0, gram)),
    Ingredient("chipolata", Amount(4, stuk)),
    Ingredient("kalkoenschnitzel", Amount(4, stuk)),
    Ingredient("kotelet", Amount(2, stuk)),
    Ingredient("biefstuk", Amount(2, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),

    Ingredient("fruit", Amount(2, stuk)),
    Ingredient("banaan", Amount(0, stuk)),
    Ingredient("appel", Amount(5, stuk)),
    Ingredient("druiven", Amount(0, doos)),
    Ingredient("persappelsienen", Amount(0, stuk)),

    Ingredient("koekjes", Amount(50, stuk)),
    Ingredient("granola", Amount(1.5, zak)),

    Ingredient("melk", Amount(5, liter)),

    Ingredient("tomaten passata", Amount(2, doos)),
    Ingredient("mais", Amount(3, blik)),
    Ingredient("zwanworstjes", Amount(1, blik)),
    Ingredient("appelmoes", Amount(2, pot)),
    Ingredient("rode kool", Amount(2, pot)),
    Ingredient("wraps", Amount(0, stuk)),

    Ingredient("mayo", Amount(0, fles)),
    Ingredient("ketchup", Amount(1, fles)),
]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None
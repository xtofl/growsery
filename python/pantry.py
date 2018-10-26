from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(36, senseo_pad)),
    Ingredient("nespresso", Amount(6, koffie_capsule)),

    Ingredient("bouillon", Amount(14*4, stuk)),
    Ingredient("groentenbouillon", Amount(34, stuk)),

    Ingredient("patat", Amount(0, stuk)),

    Ingredient("nootmuskaat", Amount(5, beetje)),

    Ingredient("currysaus", Amount(3, zakje)),
    Ingredient("kinnekessuiker", Amount(1.8, kg)),
    Ingredient("bloemsuiker", Amount(200, gram)),

    #frigo
    Ingredient("witte kool", Amount(.0, stuk)),
    Ingredient("bakboter", Amount(2, fles)),
    Ingredient("ei", Amount(1, stuk)),
    Ingredient("prei", Amount(4, stuk)),

    Ingredient("leerdammer", Amount(10, plakje)),
    Ingredient("wortel", Amount(0, stuk)),
    Ingredient("witloof", Amount(0, stuk)),
    Ingredient("ijsbergsla", Amount(0, stuk)),
    Ingredient("hamblokjes", Amount(2, doosje)),

    #kast
    Ingredient("risotto", Amount(1, kg)),
    Ingredient("basmati", Amount(.8, kg)),
    Ingredient("honing", Amount(1, pot)),

    Ingredient("bloem", Amount(3, kg)),
    Ingredient("pasta", Amount(700,gram)),
    Ingredient("krulletjes", Amount(500, gram)),
    Ingredient("vinaigrette", Amount(3, zakje)),

    Ingredient("fruit", Amount(2, stuk)),
    Ingredient("banaan", Amount(0, stuk)),
    Ingredient("appel", Amount(5, stuk)),
    Ingredient("druiven", Amount(0, doos)),
    Ingredient("persappelsienen", Amount(4, stuk)),

    Ingredient("perziken in blik", Amount(0, blik)),
    Ingredient("tomatenconcentraat", Amount(4, blik)),
    Ingredient("yoghurtjes", Amount(0, potje)),

    Ingredient("choco", Amount(2, pot)),

    Ingredient("ui", Amount(10, stuk)),

    # diepvries
    Ingredient("kroketten", Amount(2.5, zak)),

    Ingredient("diepvries broccoli", Amount(1.3, zak)),
    Ingredient("diepvrieserwten", Amount(.7, kg)),

    Ingredient("gehakt", Amount(0, gram)),
    Ingredient("kipfilet", Amount(0, gram)),
    Ingredient("chipolata", Amount(4, stuk)),
    Ingredient("kalkoenschnitzel", Amount(4, stuk)),
    Ingredient("kotelet", Amount(0, stuk)),
    Ingredient("biefstuk", Amount(0, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),

    Ingredient("koekjes", Amount(20, stuk)),
    Ingredient("granola", Amount(0.5, zak)),

    Ingredient("melk", Amount(0, liter)),
    Ingredient("melk lactosevrij", Amount(0, liter)),

    Ingredient("tomaten passata", Amount(2, doos)),
    Ingredient("mais", Amount(3, blik)),
    Ingredient("zwanworstjes", Amount(2, blik)),
    Ingredient("appelmoes", Amount(1, pot)),
    Ingredient("rode kool", Amount(2, pot)),
    Ingredient("wraps", Amount(0, stuk)),
    Ingredient("confituur", Amount(1, pot)),

    Ingredient("mayo", Amount(0, fles)),
    Ingredient("ketchup", Amount(1, fles)),
]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None
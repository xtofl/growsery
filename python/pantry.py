from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(36, senseo_pad)),
    Ingredient("nespresso", Amount(0, koffie_capsule)),

    Ingredient("bouillon", Amount(14*4, stuk)),
    Ingredient("groentenbouillon", Amount(8, stuk)),

    Ingredient("patat", Amount(10, stuk)),

    Ingredient("nootmuskaat", Amount(20, beetje)),

    Ingredient("currysaus", Amount(2, zakje)),
    Ingredient("kinnekessuiker", Amount(0, kg)),
    Ingredient("bloemsuiker", Amount(0, gram)),

    #frigo
    Ingredient("witte kool", Amount(.0, stuk)),
    Ingredient("bakboter", Amount(1, fles)),
    Ingredient("ei", Amount(16, stuk)),
    Ingredient("prei", Amount(0, stuk)),

    Ingredient("leerdammer", Amount(0, plakje)),
    Ingredient("wortel", Amount(0, stuk)),
    Ingredient("witloof", Amount(0, stuk)),
    Ingredient("ijsbergsla", Amount(0, stuk)),
    Ingredient("hamblokjes", Amount(0, doosje)),

    #kast
    Ingredient("risotto", Amount(1, kg)),
    Ingredient("basmati", Amount(.8, kg)),
    Ingredient("honing", Amount(0.5, pot)),

    Ingredient("bloem", Amount(0.2, kg)),
    Ingredient("pasta", Amount(0,gram)),
    Ingredient("krulletjes", Amount(500, gram)),
    Ingredient("vinaigrette", Amount(3, zakje)),

    Ingredient("fruit", Amount(5, stuk)),
    Ingredient("banaan", Amount(0, stuk)),
    Ingredient("appel", Amount(0, stuk)),
    Ingredient("druiven", Amount(0, doos)),
    Ingredient("persappelsienen", Amount(25, stuk)),

    Ingredient("perziken in blik", Amount(1, blik)),
    Ingredient("tomatenconcentraat", Amount(4, blik)),
    Ingredient("yoghurtjes", Amount(0, potje)),

    Ingredient("choco", Amount(0, pot)),

    Ingredient("ui", Amount(10, stuk)),

    # diepvries
    Ingredient("kroketten", Amount(0.5, zak)),

    Ingredient("diepvries broccoli", Amount(0, zak)),
    Ingredient("diepvrieserwten", Amount(.7, kg)),

    Ingredient("gehakt", Amount(0, gram)),
    Ingredient("kipfilet", Amount(0, gram)),
    Ingredient("chipolata", Amount(0, stuk)),
    Ingredient("kalkoenschnitzel", Amount(0, stuk)),
    Ingredient("kotelet", Amount(0, stuk)),
    Ingredient("biefstuk", Amount(0, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),

    Ingredient("koekjes", Amount(5, stuk)),
    Ingredient("granola", Amount(0.5, zak)),

    Ingredient("melk", Amount(5, liter)),
    Ingredient("melk lactosevrij", Amount(5, liter)),

    Ingredient("tomaten passata", Amount(3, doos)),
    Ingredient("mais", Amount(1, blik)),
    Ingredient("zwanworstjes", Amount(0, blik)),
    Ingredient("appelmoes", Amount(0, pot)),
    Ingredient("rode kool", Amount(2, pot)),
    Ingredient("wraps", Amount(0, stuk)),
    Ingredient("confituur", Amount(0, pot)),

    Ingredient("mayo", Amount(1, fles)),
    Ingredient("ketchup", Amount(1, fles)),
]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None
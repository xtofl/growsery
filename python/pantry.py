from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("bouillon", Amount(14*4, stuk)),
    Ingredient("groentenbouillon", Amount(0, stuk)),
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(30, senseo_pad)),
    Ingredient("nespresso", Amount(9, koffie_capsule)),

    Ingredient("patat", Amount(30, stuk)),

    Ingredient("currysaus", Amount(4, zakje)),

    Ingredient("nootmuskaat", Amount(30, beetje)),
    Ingredient("kinnekessuiker", Amount(1.8, kg)),
    Ingredient("bloemsuiker", Amount(200, gram)),

    #frigo
    Ingredient("witte kool", Amount(.75, stuk)),
    Ingredient("bakboter", Amount(2, fles)),
    Ingredient("ei", Amount(11, stuk)),
    Ingredient("ketchup", Amount(1, fles)),

    Ingredient("leerdammer", Amount(20, plakje)),
    Ingredient("wortel", Amount(15, stuk)),
    Ingredient("witloof", Amount(0, stuk)),

    Ingredient("risotto", Amount(.5, kg)),
    Ingredient("basmati", Amount(.3, kg)),

    Ingredient("bloem", Amount(2, kg)),
    Ingredient("pasta", Amount(1000,gram)),
    Ingredient("krulletjes", Amount(0, gram)),

    Ingredient("perziken in blik", Amount(0, blik)),
    Ingredient("tomatenconcentraat", Amount(5, blik)),
    Ingredient("yoghurtjes", Amount(0, potje)),

    Ingredient("choco", Amount(2, pot)),

    Ingredient("ijsbergsla", Amount(0, stuk)),

    Ingredient("ui", Amount(10, stuk)),

    # diepvries
    Ingredient("gehakt", Amount(0, gram)),
    Ingredient("kipfilet", Amount(800, gram)),
    Ingredient("chipolata", Amount(5, stuk)),
    Ingredient("kalkoenschnitzel", Amount(4, stuk)),
    Ingredient("kotelet", Amount(2, stuk)),
    Ingredient("biefstuk", Amount(2, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),

    Ingredient("kroketten", Amount(0, zak)),

    Ingredient("diepvries broccoli", Amount(.6, zak)),
    Ingredient("diepvrieserwten", Amount(.5, kg)),

    Ingredient("fruit", Amount(2, stuk)),
    Ingredient("banaan", Amount(0, stuk)),
    Ingredient("appel", Amount(5, stuk)),
    Ingredient("druiven", Amount(0, doos)),

    Ingredient("koekjes", Amount(12, stuk)),
    Ingredient("granola", Amount(0.1, zak)),

    Ingredient("melk", Amount(0, liter)),
    Ingredient("persappelsienen", Amount(0, stuk)),

    Ingredient("tomaten passata", Amount(4, doos)),
    Ingredient("mais", Amount(5, blik)),
    Ingredient("zwanworstjes", Amount(3, blik)),
    Ingredient("appelmoes", Amount(1, pot)),
    Ingredient("rodekool", Amount(3, pot)),
    Ingredient("wraps", Amount(10, stuk)),

    Ingredient("mayo", Amount(2, fles)),

]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None
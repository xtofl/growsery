from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(20, stuk)),
    Ingredient("nespresso", Amount(0, koffie_capsule)),

    Ingredient("bouillon", Amount(14*4, stuk)),
    Ingredient("groentenbouillon", Amount(8, stuk)),

    Ingredient("patat", Amount(20, stuk)),

    Ingredient("nootmuskaat", Amount(10, beetje)),

    Ingredient("currysaus", Amount(12, zakje)),
    Ingredient("kinnekessuiker", Amount(.8, kg)),
    Ingredient("bloemsuiker", Amount(320, gram)),
    Ingredient("puddingpoeder", Amount(3, zakje)),

    #kruiden
    Ingredient("kipkruiden", Amount(20, beetje)),
    Ingredient("pastakruiden", Amount(2, potje)),
    Ingredient("cayennepeper", Amount(0, beetje)),

    #frigo
    Ingredient("witte kool", Amount(.0, stuk)),
    Ingredient("bakboter", Amount(1, fles)),
    Ingredient("ei", Amount(1, stuk)),
    Ingredient("prei", Amount(3, stuk)),
    Ingredient("selder", Amount(3, stuk)),

    Ingredient("leerdammer", Amount(4, plakje)),
    Ingredient("wortel", Amount(12, stuk)),
    Ingredient("witloof", Amount(0, stuk)),
    Ingredient("ijsbergsla", Amount(0, stuk)),
    Ingredient("hamblokjes", Amount(0, doosje)),
    Ingredient("gerookte zalm", Amount(1, pak)),
    Ingredient("yoghurt", Amount(.5, pot)),

    #kast
    Ingredient("risotto", Amount(.7, kg)),
    Ingredient("basmati", Amount(.8, kg)),
    Ingredient("honing", Amount(1, pot)),

    Ingredient("bloem", Amount(2.2, kg)),
    Ingredient("pasta", Amount(0, gram)),
    Ingredient("spaghetti", Amount(2*250, gram)),
    Ingredient("krulletjes", Amount(250, gram)),

    Ingredient("vinaigrette", Amount(3, zakje)),

    Ingredient("fruit", Amount(0, stuk)),
    Ingredient("banaan", Amount(0, stuk)),
    Ingredient("appel", Amount(0, stuk)),
    Ingredient("druiven", Amount(0, doos)),
    Ingredient("persappelsienen", Amount(10, stuk)),

    Ingredient("perziken in blik", Amount(1, blik)),
    Ingredient("tomatenconcentraat", Amount(8, blik)),
    Ingredient("yoghurtjes", Amount(0, pot)),

    Ingredient("choco", Amount(1, pot)),

    Ingredient("ui", Amount(15, stuk)),

    # diepvries
    Ingredient("kroketten", Amount(0, zak)),

    Ingredient("diepvries broccoli", Amount(.0, zak)),
    Ingredient("diepvrieserwten", Amount(.2, kg)),

    Ingredient("gehakt", Amount(500, gram)),
    Ingredient("kipfilet", Amount(500, gram)),
    Ingredient("chipolata", Amount(5, stuk)),
    Ingredient("kalkoenschnitzel", Amount(0, stuk)),
    Ingredient("kotelet", Amount(0, stuk)),
    Ingredient("biefstuk", Amount(0, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),

    Ingredient("koekjes", Amount(15, stuk)),
    Ingredient("granola", Amount(2.5, zak)),

    Ingredient("melk", Amount(7, liter)),
    Ingredient("melk lactosevrij", Amount(6, liter)),

    Ingredient("tomaten passata", Amount(3, doos)),
    Ingredient("mais", Amount(2, blik)),
    Ingredient("zwanworstjes", Amount(0, blik)),
    Ingredient("appelmoes", Amount(0, pot)),
    Ingredient("rode kool", Amount(2, pot)),
    Ingredient("wraps", Amount(0, stuk)),
    Ingredient("confituur", Amount(2, pot)),

    Ingredient("mayo", Amount(0, fles)),
    Ingredient("ketchup", Amount(0, fles)),

    Ingredient("zakdoekjes", Amount(2, doos)),
]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None
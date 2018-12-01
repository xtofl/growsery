from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("citroenthee", Amount(1, doosje)),
    Ingredient("senseo", Amount(20, stuk)),
    Ingredient("nespresso", Amount(0, koffie_capsule)),

    Ingredient("bouillon", Amount(12*4, stuk)),
    Ingredient("groentenbouillon", Amount(8, stuk)),

    Ingredient("patat", Amount(40, stuk)),
    Ingredient("ui", Amount(15, stuk)),

    Ingredient("nootmuskaat", Amount(50, beetje)),

    Ingredient("currysaus", Amount(12, zakje)),
    Ingredient("kinnekessuiker", Amount(.8, kg)),
    Ingredient("bloemsuiker", Amount(120, gram)),
    Ingredient("puddingpoeder", Amount(3, zakje)),
    Ingredient("droge kikkererwten", Amount(500, gram)),

    Ingredient("perziken in blik", Amount(1, blik)),
    Ingredient("tomatenconcentraat", Amount(8, blik)),

    #kruiden
    Ingredient("kipkruiden", Amount(20, beetje)),
    Ingredient("pastakruiden", Amount(2, potje)),
    Ingredient("cayennepeper", Amount(50, beetje)),

    #frigo
    Ingredient("witte kool", Amount(.0, stuk)),
    Ingredient("bakboter", Amount(1, fles)),
    Ingredient("ei", Amount(4, stuk)),
    Ingredient("prei", Amount(0, stuk)),
    Ingredient("selder", Amount(0, stuk)),

    Ingredient("leerdammer", Amount(4, plakje)),
    Ingredient("wortel", Amount(6, stuk)),
    Ingredient("witloof", Amount(0, stuk)),
    Ingredient("ijsbergsla", Amount(0, stuk)),
    Ingredient("hamblokjes", Amount(0, doosje)),
    Ingredient("gerookte zalm", Amount(0, pak)),
    Ingredient("yoghurt", Amount(.5, pot)),
    Ingredient("yoghurtjes", Amount(0, pot)),

    #kast
    Ingredient("risotto", Amount(.7, kg)),
    Ingredient("basmati", Amount(.8, kg)),
    Ingredient("honing", Amount(0, pot)),

    Ingredient("bloem", Amount(2.2, kg)),
    Ingredient("pasta", Amount(0, gram)),
    Ingredient("spaghetti", Amount(2*250, gram)),
    Ingredient("krulletjes", Amount(250, gram)),

    Ingredient("vinaigrette", Amount(3, zakje)),

    Ingredient("fruit", Amount(0, stuk)),
    Ingredient("banaan", Amount(4, stuk)),
    Ingredient("appel", Amount(0, stuk)),
    Ingredient("druiven", Amount(0, doos)),
    Ingredient("persappelsienen", Amount(10, stuk)),
    Ingredient("choco", Amount(1, pot)),

    # diepvries
    Ingredient("kroketten", Amount(2, zak)),

    Ingredient("diepvries broccoli", Amount(1, zak)),
    Ingredient("diepvrieserwten", Amount(1.2, kg)),

    Ingredient("gehakt", Amount(500, gram)),
    Ingredient("kipfilet", Amount(0, gram)),
    Ingredient("chipolata", Amount(10, stuk)),
    Ingredient("kalkoenschnitzel", Amount(0, stuk)),
    Ingredient("kotelet", Amount(0, stuk)),
    Ingredient("biefstuk", Amount(0, stuk)),
    Ingredient("kippenbout", Amount(0, stuk)),

    Ingredient("koekjes", Amount(15, stuk)),
    Ingredient("granola", Amount(1.5, zak)),

    Ingredient("melk", Amount(0, liter)),
    Ingredient("melk lactosevrij", Amount(0, liter)),

    Ingredient("tomaten passata", Amount(2, doos)),
    Ingredient("mais", Amount(0, blik)),
    Ingredient("zwanworstjes", Amount(0, blik)),
    Ingredient("appelmoes", Amount(1, pot)),
    Ingredient("rode kool", Amount(2, pot)),
    Ingredient("wraps", Amount(12, stuk)),
    Ingredient("confituur", Amount(1, pot)),

    Ingredient("mayo", Amount(0, fles)),
    Ingredient("ketchup", Amount(1, fles)),

    Ingredient("zakdoekjes", Amount(2, doos)),
]

def from_pantry(pantry, ingredient):
    try:
        zero = ingredient.zero()
        return sum( (i for i in pantry if i.name == ingredient.name), zero)
    except StopIteration:
        return None

def test_from_pantry_finds_ingredients():
    one = Amount(1, stuk)
    a = Ingredient("A", one)
    b = Ingredient("B", one)
    pantry = [a, b]
    assert from_pantry(pantry, a) == a
    assert from_pantry(pantry, b) == b
    assert Ingredient("not there", Amount(0, stuk)) == from_pantry(pantry, Ingredient("not there", one))

    pantry = [a, a]
    assert from_pantry(pantry, a) == Ingredient("A", Amount(2, stuk))
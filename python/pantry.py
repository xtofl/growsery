from entities import *
from units import *
from recipes import *

pantry = [
    Ingredient("bouillon", Amount(8, stuk)),
    Ingredient("citroenthee", Amount(0, doosje)),
    Ingredient("senseo", Amount(40, senseo_pad)),
    Ingredient("nespresso", Amount(9, koffie_capsule)),

    Ingredient("patat", Amount(40, stuk)),

    Ingredient("currysaus", Amount(5, zakje)),

    Ingredient("nootmuskaat", Amount(30, beetje)),

    #frigo
    Ingredient("witte kool", Amount(.75, stuk)),
    Ingredient("bakboter", Amount(1, fles)),
    Ingredient("ei", Amount(15, stuk)),
    Ingredient("ketchup", Amount(0, fles)),

    Ingredient("risotto", Amount(1., kg)),
    Ingredient("basmati", Amount(1., kg)),

    Ingredient("bloem", Amount(.8, kg)),
    Ingredient("pasta", Amount(1000,gram)),
    Ingredient("krulletjes", Amount(0, gram)),

    Ingredient("perziken in blik", Amount(0, blik)),
    Ingredient("tomatenconcentraat", Amount(2, blik)),
    Ingredient("yoghurtjes", Amount(0, potje)),

    Ingredient("choco", Amount(2, pot)),

    Ingredient("ijsbergsla", Amount(0, stuk)),

    Ingredient("ui", Amount(20, stuk)),

    Ingredient("gehakt", Amount(300, gram)),
    Ingredient("kipfilet", Amount(1000, gram)),
    Ingredient("chipolata", Amount(15, stuk)),
    Ingredient("kippenbout", Amount(3, stuk)),
    Ingredient("kalkoenschnitzel", Amount(4, stuk)),
    Ingredient("kotelet", Amount(2, stuk)),
    Ingredient("biefstuk", Amount(2, stuk)),

    Ingredient("kroketten", Amount(0, zak)),

    Ingredient("diepvries broccoli", Amount(0, zak)),
    Ingredient("diepvrieserwten", Amount(.5, kg)),

    Ingredient("fruit", Amount(2, stuk)),
    Ingredient("banaan", Amount(4, stuk)),
    Ingredient("appel", Amount(16, stuk)),
    Ingredient("druiven", Amount(2, doos)),
    
    Ingredient("koekjes", Amount(12, stuk)),
    Ingredient("granola", Amount(0.1, zak)),

    Ingredient("melk", Amount(0, liter)),
    Ingredient("persappelsienen", Amount(0, stuk)),

    Ingredient("tomaten passata", Amount(4, doos)),
    Ingredient("mais", Amount(5, blik)),
    Ingredient("zwanworstjes", Amount(3, blik)),
    Ingredient("appelmoes", Amount(1, pot)),
    Ingredient("rodekool", Amount(4, pot)),
    Ingredient("wraps", Amount(2, pak)),

    Ingredient("koekjes", Amount(12, stuk)),
    Ingredient("mayo", Amount(2, fles)),

]

def from_pantry(pantry, ingredient):
    try:
        return next(i for i in pantry if i.name == ingredient.name)
    except StopIteration:
        return None
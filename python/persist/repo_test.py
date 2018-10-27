from entities import Ingredient
from entities import Amount
from entities import Unit
from persist import JsonStore

def test_can_load_growsery_list():
    groceries = [Ingredient(name="Batterij", amount=Amount(2, Unit("stuk")))]
    db = JsonStore()
    stored = db.store(groceries)
    restored = db.restore(stored)

    assert(groceries == restored)
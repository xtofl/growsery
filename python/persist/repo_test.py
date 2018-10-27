from entities import Ingredient
from entities import Amount
from entities import Unit
from persist import JsonStore

def test_unit():
    db = JsonStore()
    sample_unit = Unit("zample")
    for unit in [
            Unit("x", conversions={sample_unit: lambda x: 2*x}),
            Unit("y", conversions={sample_unit: lambda x: x+3})]:
        to_sample = unit.to(sample_unit)(10)
        stored = db.store(unit)
        restored = db.restore(stored)
        assert(type(restored) == type(unit))
        assert(restored.label == unit.label)
        assert(restored.to(sample_unit)(10) == to_sample)

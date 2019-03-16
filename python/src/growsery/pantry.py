#!/usr/bin/env python3
from entities import *
from units import *
from recipes import *
import pytest

def pantry_lines(pantry_string):
    lines = map(str.strip, pantry_string.splitlines(keepends=False))
    return list(line for line in lines if len(line) and not line.startswith("#"))
    assert all(len(s.split(":")) == 2 for s in lines)

def test_pantry_lines():
    assert ["a: 1 x", "b B: 3 y"] == list(pantry_lines("""
    a: 1 x
    b B: 3 y
    """))
    assert [] == list(pantry_lines("#dont forward comments"))

def pantry_items(pantry_lines, units):
    return [
        Ingredient(name, Amount(float(n), units[u]))
            for name, n, u in map(pantry_item_chunks, pantry_lines)
        ]

def pantry_item_chunks(pantry_line):
    name, amount_str = pantry_line.split(":")
    n, unit_str = amount_str.split()
    return (name, n, unit_str)

def test_pantry_item_chunks():
    a, b, c = pantry_item_chunks("b B: 2 y")
    assert ("b B", "2", "y") == (a, b, c)
    a, b, c = pantry_item_chunks("a: 1 x")

def test_pantry_items():
    x = Unit("x")
    y = Unit("y")
    items = pantry_items(["a: 1 x", "b B: 2 y"], {"x": x, "y": y})
    assert items[0] == Ingredient("a", Amount(1, x))
    assert items[1] == Ingredient("b B", Amount(2, y))

    items = pantry_items(pantry_lines("""
kippenkruiden: 100 beetje
komijn: 100 beetje
droge kikkererwten: 600 gram
"""), {"beetje": beetje, "gram": gram})
    assert len(items) == 3


units = {
    "beetje": beetje,
    "plakje": plakje,
    "capsule": capsule,
    "liter": liter,
    "pak": pak,
    "kg": kg,
    "gram": gram,
    "g": g,
    "fles": fles,
    "zakje": zakje,
    "zak": zak,
    "doos": doos,
    "koffie_capsule": koffie_capsule,
    "pot": pot,
    "blik": blik,
    "stuk": stuk,
}


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


def test_from_pantry_counts_all_lines_with_same_ingredient():
    pantry = pantry_items(pantry_lines("""
    # frigo
    confituur: 1 pot
    # berging:
    confituur: 1 pot
    """), units)
    assert Amount(2, pot) == from_pantry(pantry, Ingredient("confituur", Amount(0, pot))).amount


def collect(pantry):
    keys = set(map(Ingredient.zero, pantry))
    return (from_pantry(pantry, i) for i in keys)


def from_file(filename):
    with open(filename, "r") as f:
        pantry_string = f.read()
        return collect(pantry_items(pantry_lines(pantry_string), units))

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "r") as f:
        ingredients = list(from_file(sys.argv[1]))
        print("\n".join(str(i) for i in ingredients))
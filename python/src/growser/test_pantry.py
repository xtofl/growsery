#!/usr/bin/env python3
from growser.pantry import *
import pytest

def test_pantry_lines():
    assert ["a: 1 x", "b B: 3 y"] == list(pantry_lines("""
    a: 1 x
    b B: 3 y
    """))
    assert [] == list(pantry_lines("#dont forward comments"))

def test_pantry_item_chunks():
    a, b, c = pantry_item_chunks("b B: 2 y")
    assert ("b B", "2", "y") == (a, b, c)
    a, b, c = pantry_item_chunks("a: 1 x")

"""A database of units"""
from .entities import Unit
from .entities import Amount


#units
gram = Unit("g")
g = gram
kg = Unit("kg", {gram: lambda kg: kg*1000.})

fles = Unit("fles")

stuk = Unit("stuk")

liter = Unit("liter")

plakje = Unit("plakje")
pot = Unit("pot")
potje = pot
bakje = Unit("bakje")
blik = Unit("blik")
blikje = blik
teentje = Unit("teentje")

zak = Unit("zak")
zakje = zak
pak = Unit("pak")
pakje = pak

senseo_pad = Unit("pad")
koffie_capsule = Unit("capsule")
capsule = koffie_capsule
doos = Unit("doos")
doosje = doos

takje = Unit("takje")

beetje = Unit("beetje", {
    liter: lambda x: x/100,
    fles: lambda x: x/100
})

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

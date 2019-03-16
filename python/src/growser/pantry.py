#!/usr/bin/env python3
from .entities import *
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

def from_pantry(pantry, ingredient):
    try:
        zero = ingredient.zero()
        return sum( (i for i in pantry if i.name == ingredient.name), zero)
    except StopIteration:
        return None

def collect(pantry):
    keys = set(map(Ingredient.zero, pantry))
    return (from_pantry(pantry, i) for i in keys)


def from_file(filename, units):
    with open(filename, "r") as f:
        pantry_string = f.read()
        return collect(pantry_items(pantry_lines(pantry_string), units))

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "r") as f:
        ingredients = list(from_file(sys.argv[1]))
        print("\n".join(str(i) for i in ingredients))
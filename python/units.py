from entities import *


#units
gram = Unit("g")
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
doos = Unit("doos")
doosje = doos

takje = Unit("takje")

beetje = Unit("beetje", {
    liter: lambda x: x/100,
    fles: lambda x: x/100
})

koffielepel = Unit("kl", {
    beetje: lambda x: x
})
eetlepel = Unit("el", {
    koffielepel: lambda x: 5*x
})

def test_units():
    assert Amount(100, beetje) - Amount(1, fles) == Amount.zero

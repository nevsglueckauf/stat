import numpy as np
from textfoo import Texitfy

print("Eine Integer-Zahl: ", np.random.randint(1, 7000))

print(
    "\nWie eben, aber alternative size-Definition:\n",
    np.random.randint(1, 5300, size=(10,)),
)

print("\nZweidimensionales Array:\n", np.random.randint(1, 10000, size=(5, 4)))

foo = {
    "bar": 42,
    "lol": 374893,
}

print(foo)

names = [
    "Beulah",
    "Branden",
    "Druci",
    "Carolina",
    "Aloin",
    "Brok",
    "Dorotea",
    "Deena",
    "Syman",
    "Lynette",
    "Batholomew",
    "Darcee",
    "Whitney",
    "Robbie",
    "Reina",
    "Kinnie",
    "Jeni",
    "Fabio",
    "Vinni",
    "Jamie",
    "Evelin",
    "Shea",
    "Jenine",
    "Almeda",
    "Yance",
    "Mallorie",
    "Darcie",
    "Dermot",
    "Elisabeth",
    "Orlan",
    "Erasmus",
    "Eustace",
    "Alyssa",
    "Ulysses",
    "Merell",
    "Selia",
    "Amelie",
    "Jermain",
    "Zarah",
    "Betti",
    "Fidel",
    "Iona",
    "Vivianna",
    "Nelly",
    "Kevyn",
    "Nickolas",
    "Athene",
    "Angeline",
    "Frederica",
    "Merrie",
    "Jere",
    "Laraine",
    "Wildon",
    "Bartolemo",
    "Adriaens",
    "Nikolaus",
    "Everett",
    "Sherri",
    "Lamar",
    "Mortimer"
]

min = 148
max = 199
for name in names:
    print(Texitfy.quote(name) + ":" + str(np.random.randint(min, max)) + ",")

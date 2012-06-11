#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Juhani Numminen <juhaninumminen0@gmail.com>
# License: GNU GPL v3+

import random

from langtools.gen import *

print("Finnish:")

for i in range(1, random.randint(5, 15)):
    if i == 1:
        print(generate_word_fi().capitalize(), end="")
    elif random.randint(1, 5) == random.randint(1, 3):
        print(" ", generate_word_fi(), ",", sep="", end="")
    else:
        print(" ", generate_word_fi(), sep="", end="")
print(" ", generate_word_fi(), sep="", end="")
print(".")

print("Estonian:")

for i in range(1, random.randint(5, 15)):
    if i == 1:
        print(generate_word_et().capitalize(), end="")
    elif random.randint(1, 5) == random.randint(1, 3):
        print(" ", generate_word_et(), ",", sep="", end="")
    else:
        print(" ", generate_word_et(), sep="", end="")
print(" ", generate_word_et(), sep="", end="")
print(".")

print("German:")

for i in range(1, random.randint(5, 15)):
    if i == 1:
        print(generate_word_de().capitalize(), end="")
    elif random.randint(1, 5) == random.randint(1, 3):
        print(" ", generate_word_de(), ",", sep="", end="")
    else:
        print(" ", generate_word_de(), sep="", end="")
print(" ", generate_word_de(), sep="", end="")
print(".")

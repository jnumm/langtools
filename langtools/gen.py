# -*- coding: utf-8 -*-

# Copyright (C) 2012 Juhani Numminen <juhaninumminen0@gmail.com>
# License: GNU GPL v3+

"""Not very scientific word generator

Includes functions to generate "words" of a few languages.
Just kidding! If you can read these languages, you quickly notice that
the output is just rubbish.

These are not written to offence people who are from these countries.
"""

import random

# Define the constants, which are word and sentence classes.
RANDOM = "random"

WORD_NOUN = "noun"
WORD_PRONOUN = "pronoun"
WORD_ADJECTIVE = "adjective"
WORD_VERB = "verb"
WORD_ADVERB = "adverb"
WORD_PREPOSITION = "preposition"
WORD_CONJUNCTION = "conjunction"
WORD_INTERJECTION = "interjection"
WORD_NUMERAL = "numeral"
WORD_TYPES = [WORD_NOUN, WORD_VERB, WORD_ADVERB, WORD_PREPOSITION,
        WORD_CONJUNCTION, WORD_INTERJECTION, WORD_NUMERAL]

SENTENCE_DECLARATIVE = "declarative"
SENTENCE_INTERROGATIVE = "interrogative"
SENTENCE_EXCLAMATORY = "exclamatory"

SUPPORTED_LANGS = ["de", "et", "fi"]

def generate_word(lang=RANDOM, word_type=RANDOM):
    """Helper function for word generation
    
    This function calls the appropriate function for the selected
    language. Language is a *nix locale-style (fi, en_US, pt_BR etc.)
    code.
    
    If the language is not supported, a ValueError is raised.
    """
    
    if lang == RANDOM:
        lang = random.sample(SUPPORTED_LANGS, 1)[0]
    elif lang not in SUPPORTED_LANGS:
        raise ValueError("language '{}' is not supported".format(lang))
    assert lang in SUPPORTED_LANGS
    
    if lang == "de":
        return generate_word_de(word_type=word_type)
    elif lang == "et":
        return generate_word_et(word_type=word_type)
    elif lang == "fi":
        return generate_word_fi(word_type=word_type)
    
    # This should never get executed, assertion just to be sure.
    assert True == False

def generate_word_de(word_type=RANDOM):
    """Generate a word which souds a bit German.
    
    The words are generated one syllable at a time.
    This function makes heavy use of the 'random' module.
    """
    
    word = ""
    
    if word_type == RANDOM:
        word_type = random.sample(WORD_TYPES, 1)[0]
    
    for i in range(1, random.randint(2, 6)):
        letter1 = letter2 = letter3 = ""
        
        if ("ä" or "ö") in word:
            letter1 = random.choice("bbbeehiijklmnnprsttvyäö")
        else:
            letter1 = random.choice("abbbbcccdeefghiijjkklmnnnoprsttuväöü")
        
        if (("a" or "e" or "i" or "o" or "u" or "ä" or "ö" or "ü")
                not in letter1):
            if random.randint(1, 7) == random.randint(1, 3):
                letter2 = letter1
            else:
                letter2 = random.choice("aeiouäöü")
            
            if (("a" or "e" or "i" or "o" or "u" or "ä" or "ö" or "ü")
                    in letter2):
                letter3 = random.choice("bcdhjklmnnnoprsssttvw")
        else:
            letter2 = random.choice("hkllmnnprssstvww")
        
        word += letter1 + letter2 + letter3
        
        if random.randint(1, 5) == random.randint(1, 3):
            word += "sch"
    
    word = word.replace("ss", "ß")
    
    if word_type == WORD_VERB:
        word += "en"
    elif word_type == WORD_NOUN:
        word = word.capitalize()
        
        if random.randint(1, 4) == 1:
            word = "der " + word
        elif random.randint(1, 3) == 1:
            word = "das " + word
        elif random.randint(1, 2) == 1:
            word = "die " + word
        
        if random.randint(2, 3) == random.randint(1, 9):
            word = word.translate(str.maketrans({"a": "ä", "o": "ö",
                    "u": "ü"}))
            word += "chen"
    
    return word

def generate_word_et(word_type=RANDOM):
    """Generate a word which souds a bit Estonian.
    
    The words are generated one syllable at a time.
    This function makes heavy use of the 'random' module.
    """
    
    word = ""
    
    if word_type == RANDOM:
        word_type = random.sample(WORD_TYPES, 1)[0]
    
    for i in range(1, random.randint(3, 5)):
        letter1 = letter2 = letter3 = ""
        
        if ("ä" or "ö") in word:
            letter1 = random.choice("eehiijklmnnprsttvyäö")
        else:
            letter1 = random.choice("aaeeghiijjkkkllmnnnnooprsttuvõäöü")
        
        if (("a" or "e" or "i" or "o" or "u" or "õ" or "ä" or "ö" or "ü")
                not in letter1):
            letter2 = random.choice("aeiouõäöü")
            if (("a" or "e" or "i" or "o" or "u" or "y" or "ä" or "ö")
                    in letter2):
                letter3 = random.choice("hjklmnnnoprsssttv")
        else:
            letter2 = random.choice("hkllmnnprssst")
        
        word += letter1 + letter2 + letter3
    
    if random.randint(1, 5) == random.randint(1, 3):
        word += "ga"
    return word

def generate_word_fi(word_type=RANDOM):
    """Generate a word which souds a bit Finnish.
    
    The words are generated one syllable at a time.
    This function makes heavy use of the 'random' module.
    """
    
    word = ""
    
    if word_type == RANDOM:
        word_type = random.sample(WORD_TYPES, 1)[0]
    
    for i in range(1, random.randint(3, 6)):
        letter1 = letter2 = letter3 = ""
        
        if ("ä" or "ö") in word:
            letter1 = random.choice("eehiijklmnnprsttvyäö")
        else:
            letter1 = random.choice("aaeehiijjkkkllmnnnnoprsttuvyäö")
        
        if (("a" or "e" or "i" or "o" or "u" or "y" or "ä" or "ö")
                not in letter1):
            letter2 = random.choice("aaaeeeiiiioouuyäö")
            if (("a" or "e" or "i" or "o" or "u" or "y" or "ä" or "ö")
                    in letter2):
                letter3 = random.choice("hjklmnnnoprsssttv")
        else:
            letter2 = random.choice("hkllmnnprssst")
        
        word += letter1 + letter2 + letter3
    
    word = word.replace("ee", "ie").replace("öö", "yö").replace("oo",
            "oe").replace("ii", "ie")
    
    if random.randint(1, 5) == random.randint(1, 3):
        word += "isi"
    if word_type == WORD_VERB:
        word += "imme"
    return word

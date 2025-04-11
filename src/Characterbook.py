from Character import *
from Movebook import characters_book as book

def create_agatha() :
    ag_tablet = get_tablet(generate_key(4))
    ag_moveset = book["agatha"]
    global agatha
    agatha = Character("Agatha", 85, 85, 5, ag_tablet, ag_moveset)

def create_sak_pixan() :

    sp_tablet = get_tablet(generate_key(6))
    sp_moveset = book["sak_pixan"]
    global sak_pixan 
    sak_pixan = Character("Sak Pixan", 140, 140, 4, sp_tablet, sp_moveset)

def create_you() :
    yu_tablet = get_tablet(generate_key(6))
    yu_moveset = book["you"]
    global you
    you = Character("'You' is a suitable name", 10, 10, 8, yu_tablet, yu_moveset)
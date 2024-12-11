from Character import *

def create_agatha() :
    ag_tablet = get_tablet(generate_key(4))
    ag_moveset = [  Move("Shatter", 30, -25, "tsh"),
                    MoveExt("Drown", False, 60, 10, -15, 1, "ttt"),
                    Move("Bandage", 0, 35, "sssh")]
    global agatha
    agatha = Character("Agatha", 85, 85, 5, ag_tablet, ag_moveset)

def create_sak_pixan() :

    sp_tablet = get_tablet(generate_key(6))
    sp_moveset = [  MoveExt("Vacant eyes", True, -10, 3, 30, 3, "mnc"),
                    Rotate("Presence: Rotate", 1, 1, "", Move("Presence: Somewhere", 10, 0, "")),
                    Move("Presence: as lanterns take flight", 35, 35, "ssmmtcn"),
                    MoveExt("'My world had ended long ago.'", False, 85, 10, -85, 3, "ccctttnnn")] 
    global sak_pixan 
    sak_pixan = Character("Sak Pixan", 140, 140, 4, sp_tablet, sp_moveset)

def create_you() :
    yu_tablet = get_tablet(generate_key(6))
    yu_moveset = [  Rotate("all my wishes ", 1, 1, "hmn", MoveExt("for Harmony", True, 10, 2, -1, 1, "")),
                    Rotate("illustrated ", 2, 2, "hmnst", MoveExt("Lies;", True, 35, 1, -2, 1, "" )),                    
                    Rotate("within ", 3, 3, "hhhcc", MoveExt("depth", True, 20, 3, -5, 1, "")),
                    MoveExt("blind", True, 150, 1, -10, 1, "hhhhccnn" ),
                    MoveExt("a world that's broken down; The Garden of Choice", True, 150, 1, -100, 10, "hhhcccmmnnst")]
    global you
    you = Character("'You' is a suitable name", 10, 10, 8, yu_tablet, yu_moveset)
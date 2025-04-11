from Move_Rotate import *

characters_book = {
    "agatha" : [
        Move("Shatter", 30, -25, "tsh"),
        MoveExt("Drown", False, 60, 10, -15, 1, "ttt"),
        Move("Bandage", 0, 35, "sssh")
        #MoveExt("Sundown", True, (100 - current%hp) * emotion_level, all, 0, 1, cost=locked )
    ],
    "sak_pixan" : [
        MoveExt("Vacant eyes", True, -10, 3, 30, 3, "mnc"),
        Rotate("Presence: Rotate", 1, 1, "", Move("Presence: Somewhere", 10, 0, "")),
        Move("Presence: as lanterns take flight", 35, 35, "ssmmtcn"),
        MoveExt("'My world had ended long ago.'", False, 85, 10, -85, 3, "ccctttnnn")
    ],
    "you" : [
        Rotate("all my wishes ", 1, 1, "hmn", MoveExt("for Harmony", True, 10, 2, -1, 1, "")),
        Rotate("illustrated ", 2, 2, "hmnst", MoveExt("Lies;", True, 35, 1, -2, 1, "" )),
        Rotate("within ", 3, 3, "hhhcc", MoveExt("depth", True, 20, 3, -5, 1, "")),
        MoveExt("blind", True, 150, 1, -10, 1, "hhhhccnn" ),
        MoveExt("a world that's broken down; The Garden of Choice", True, 150, 1, -100, 10, "hhhcccmmnnst")
    ]
}

enemy_book_1 = {
    "wind_spirits" : {
        Move("Fuwafuwa", 15, 0, ""),
        Move("Not fade away", 25, 5, ""),
        Move("Help", 0, 15, "")
    }
}


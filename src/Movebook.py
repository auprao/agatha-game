from Move_Rotate import *

characters_book = {
    "agatha" : [
        Move("Shatter", 30, -25, "tsh"),
        Move("Drown", 60, -15, "ttt", directed=False, enemy_targets=10),
        Move("Bandage", 0, 35, "sssh")
        #MoveExt("Sundown", (100 - current%hp) * emotion_level, all, 0, 1, cost=locked )
    ],
    "sak_pixan" : [
        Move("Vacant eyes", -10, 30, "mnc", enemy_targets=3, team_targets=3),
        Rotate("Presence: Rotate", 1, 1, "", Move("Presence: Somewhere", 10, 0, "")),
        Move("Presence: as lanterns take flight", 35, 35, "ssmmtcn"),
        Move("'My world had ended long ago.'", 85, -85, "ccctttnnn", enemy_targets=10, team_targets=3)
    ],
    "you" : [
        Rotate("all my wishes ", 1, 1, "hmn", Move("for Harmony", 10, -1, "", enemy_targets=2)),
        Rotate("illustrated ", 2, 2, "hmnst", Move("Lies;", 35, -2, "" )),
        Rotate("within ", 3, 3, "hhhcc", Move("depth", 20, -5, "", enemy_targets=3)),
        Move("blind", 150, -10, "hhhhccnn" ),
        Move("a world that's broken down; The Garden of Choice", 150, -100, "hhhcccmmnnst", team_targets=10)
    ]
}

enemy_book_1 = {
    "wind_spirits" : {
        Move("Fuwafuwa", 15, 0, ""),
        Move("Not fade away", 25, 5, ""),
        Move("Help", 0, 15, "")
    }
}


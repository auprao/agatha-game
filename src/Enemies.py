from Enemy import Enemy
from Main import Move

class WindSpirit(Enemy) :
    def __init__(self):
        w_spirit_moveset = [Move("Fuwafuwa", 15, 0, ""),
                          Move("Not fade away", 25, 5, ""),
                          Move("Help", 0, 15, "")]
        super().__init__("Wind Spirit", 60, 4, w_spirit_moveset)
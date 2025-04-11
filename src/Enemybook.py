from Enemy import Enemy
from Movebook import enemy_book_1 as book_1

class WindSpirit(Enemy) :
    def __init__(self):
        w_spirit_moveset = book_1["wind_spirits"]
        super().__init__("Wind Spirit", 60, 4, w_spirit_moveset)
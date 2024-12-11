from Tablet_Cost_Resources import *
from Enemy import *
from Enemies import *
from Move_Rotate import *
from Encounter import *
from Characters import *

def main() : 

    create_agatha()
    create_sak_pixan()
    create_you()

    e1_enemies = [WindSpirit(), WindSpirit(), WindSpirit()]

    print("First Encounter!")
    encounter(characters, e1_enemies)

# add the cover up stones n name them ("stone" ?)
# agatha, unable
# error handle selecting target
# write execute_move in Move
# write read_moveset in Character

if __name__ == "__main__":
    main()
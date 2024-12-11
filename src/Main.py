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

# finish reading move
# add the cover up stones n name them
# agatha, unable
# error handle selecting target
# todo: make wait move a rotate (0 times) to not ask for target
# write execute_move in Move
# move character to Character.py (global difficulties)
# is it ok to import * ? should it import only the necessary specific code?

if __name__ == "__main__":
    main()
from Encounter import *
from Characterbook import *
from Enemybook import *

def main() : 

    create_agatha()
    create_sak_pixan()
    create_you()

    e1_enemies = [WindSpirit(), WindSpirit(), WindSpirit()]

    print("\nFirst Encounter!")
    encounter(characters, e1_enemies)

# add the cover up stones n name them ("stone" ?)
# error handle selecting target
# write execute_move in Move
# write read_moveset in Character
# emotion level
# make every Move into MoveExt, have actual MoveExt that works with turn count, hp, all char traits
# apply status effects

if __name__ == "__main__":
    main()
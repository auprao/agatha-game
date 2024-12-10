from Tablet_Cost_Resources import *
from Enemy import *
from Enemies import *
from Move_Rotate import *
from Encounter import *

characters = []

class Character :
    def __init__(self, name, max_hp, hp, speed, tablet, moveset) :
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.speed = speed
        self.tablet = tablet
        self.moveset = moveset
        self.resources = ""
        moveset.append(Move("Wait", 0, 0, ""))
        moveset.append(Rotate("Rotate", 1, 1, "c", None))
        characters.append(self)

    def choose_move(self, resources, enemies) :

        #present moves
        print(f"{self.name}'s moveset:")
        for i in range(len(self.moveset)) :
            print(f"Move {i + 1}: {self.read_moveset(i)}")

        full_target = None
        chosen = False
        while not chosen :
            #let choose
            choice = int(input(f"Type (1,2...) to choose the move for {self.name}: "))
            if 0 < choice <= len(self.moveset):
                print(f'Move "{self.moveset[choice - 1].name}" chosen.')

                #check cost
                if are_resources_enough(self.moveset[choice - 1].cost, resources) :
                    if isinstance(self.moveset[choice - 1], Rotate) :
                        print("rotated")
                        #make stone rotate (not tablet)
                    elif self.moveset[choice - 1].directed :
                        target_valid = False
                        while not target_valid :
                            target = input("Choose an enemy target, by full name: ")
                            for i in range(len(enemies)):
                                if target in enemies[i].name and not target_valid :
                                    print(f"{target} chosen.")
                                    full_target = enemies[i]
                                    target_valid = True
                            # imperfect looping
                    chosen = True
                else :
                    print(f'Not enough resources for "{self.moveset[choice - 1].name}", try again!')

            else : 
                print("Invalid move, try again!")

        return self.moveset[0], full_target

    def read_moveset(self, i) :
        current = self.moveset[i]
        readable = f'"{current.name}", '
        if isinstance(current, Move) or isinstance(current, MoveExt) :
            readable += f"{current. dmg} DMG, {current.heal} healing"

            if isinstance(current, MoveExt) :
                pass
            else :
                pass
        else:
            readable += f'{current.times} times'

        return readable + f", cost - {read_cost(current.cost)}"

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
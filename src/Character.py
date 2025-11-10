from Move_Rotate import *
from Tablet_Cost_Resources import *


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
        moveset.append(Rotate("Wait", 0, 0, "")) 
        moveset.append(Rotate("Rotate", 1, 1, "c"))
        characters.append(self)

    def choose_move(self, resources, enemies) :

        #present moves
        print(f"\n{self.name}'s moveset:")
        for i in range(len(self.moveset)) :
            print(f"Move {i + 1}: {self.read_move(i)}")

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

    def read_move(self, i) :
        current = self.moveset[i]
        readable = f'"{current.name}", '
        if isinstance(current, Move)  :
            readable += f"{current. dmg} DMG"
            if current.selfdmg < 0 :
                readable += f", {-current.selfdmg} healing"
            elif current.selfdmg < 0 :
                readable += f", {current.selfdmg} self-damage"

            # should have extra readables

        else:
            readable += f'{current.times} times'

        return readable + f", cost - {read_cost(current.cost)}"
    
def sort_by_speed(chars) :
    for c in range(len(chars) - 1) :
        for i in range(len(chars) - 1) :
            if chars[i].speed < chars[i + 1].speed :
                temp = chars[i]
                chars[i] = chars[i + 1]
                chars[i + 1] = temp
    return chars

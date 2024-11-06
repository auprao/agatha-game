import math
import random

def fill_tablet(length) :
    tablet = []
    for i in range(length) :
        tablet.append([])
        for j in range(length) :
            tablet[i].append("")
    return tablet

def get_tablet(key) :
    length = int(math.sqrt(len(key)))
    tablet = fill_tablet(length)
    current = [0, 0]
    for s in range(len(key)) :
        current[0] = s // length
        current[1] = s % length
        match key[s] :
            case "e" :
                tablet[current[0]][current[1]] = "empty"
            case "s" :
                tablet[current[0]][current[1]] = "star"
            case "t" :
                tablet[current[0]][current[1]] = "tide"
            case "c" :
                tablet[current[0]][current[1]] = "cycle"
            case "m" :
                tablet[current[0]][current[1]] = "moon"   
            case "n" :
                tablet[current[0]][current[1]] = "nature"
            case "h" :
                tablet[current[0]][current[1]] = "heart"       
    return tablet

def print_tablet(tablet) : 
    for i in range(len(tablet)) :
        for j in range(len(tablet)) :
            current = tablet[i][j]
            match current :
                case "empty" :
                    print("  ", end = " ")
                case "star" :
                    print(" ☆", end = " ")
                case "tide" :
                    print(" ࿐", end = " ")
                case "cycle" :
                    print(" ○", end = " ")
                case "moon" :
                    print(" ☾", end = " ")
                case "nature" :
                    print(" ⚶", end = " ")
                case "heart" :
                    print(" ♡", end = " ")
        print("")

def read_cost(cost):
    symbols = ""
    cost = sorted(cost)
    for i in range(len(cost)) :
        current = cost[i]
        match current :
                case "s" :
                    symbols += "☆ "
                case "t" :
                    symbols += "࿐ "
                case "c" :
                    symbols += "○ "
                case "m" :
                    symbols += "☾ "
                case "n" :
                    symbols += "⚶ "
                case "h" :
                    symbols += "♡ "
    return symbols

def generate_key(length) :
    key = ""
    chars = ["s","t","c","m","n","h"]
    for i in range(len(chars)*2) :
        chars.append("e")
    for i in range(length ** 2) :
        key = key + random.choice(chars)
    return key


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


class Enemy :
    def __init__(self, name, hp, speed, moveset) :
        self.name = name
        self.hp = hp
        self.speed = speed
        self.moveset = moveset

    def choose_move(self, enemies) :

        target = None

        choice = random.randint(1,len(self.moveset))
        print(f'{self.name} chose "{self.moveset[choice - 1].name}".')

        if self.moveset[choice - 1].directed :
            target = random.choice(enemies)
            print(f"{self.name} chose {target.name} as their target!")

        return self.moveset[0], target

class WindSpirit(Enemy) :
    def __init__(self):
        w_spirit_moveset = [Move("Fuwafuwa", 15, 0, ""),
                          Move("Not fade away", 25, 5, ""),
                          Move("Help", 0, 15, "")]
        super().__init__("Wind Spirit", 60, 4, w_spirit_moveset)

def sort_by_speed(chars) :
    for j in range(len(chars) - 1) :
        for i in range(len(chars) - 1) :
            if chars[i].speed < chars[i + 1].speed :
                temp = chars[i]
                chars[i] = chars[i + 1]
                chars[i + 1] = temp
    return chars

def get_resources(tablet) :
    new_resources = ""
    for i in range(len(tablet)) :
        for j in range(len(tablet)) :
            char = ""
            match tablet[i][j] :
                case "empty" :
                    char = ""
                case "star" :
                    char = "s"
                case "tide" :
                    char = "t"
                case "cycle" :
                    char = "c"
                case "moon" :
                    char = "m"
                case "nature" :
                    char = "n"
                case "heart" :
                    char = "h"

            new_resources += char
    return new_resources
    
def are_resources_enough(cost, resources) :
    for i in range(len(cost)) :
        found = False
        j = 0
        while j < (len(resources)) and len(cost) > 0 and not found:
            if cost[0] == resources[j]:
                resources = resources[:j] + resources[j+1:]
                cost = cost[1:]
                found = True
            j += 1
        if not found :
            return False
    return True

def delete_cost(cost, resources) :
    for i in range(len(cost)) :
        j = 0
        found = False
        while not found :
            if cost[i] == resources[j]:
                found = True
                resources.replace(resources[j], "")
            j += 1
    return resources
    
class Move :
    def __init__(self, name, dmg, heal, cost) :
        self.name = name
        self.directed = True
        self.dmg = dmg
        self.enemy_targets = 1
        self.heal = heal
        self.team_targets = 1
        self.cost = cost

class MoveExt :
    def __init__(self, name, directed, dmg, enemy_targets, heal, team_targets, cost) :
        self.name = name
        self.directed = directed
        self.dmg = dmg
        self.enemy_targets = enemy_targets
        self.heal = heal
        self.team_targets = team_targets
        self.cost = cost
# MoveExt("name", directed bool, dmg, enemy_targets. heal, team_targets, cost)

class Rotate :
    def __init__(self, name, times, team_targets, cost, move) :
        self.name = name
        self.times = times
        self.team_targets = team_targets
        self.cost = cost
        self.move = move

def get_move_cost(key) :
    resources = []
    for i in range(len(key)) :
        match key[i] :
            case "s" :
                resources.append("star")
            case "t" :
                resources.append("tide")
            case "c" :
                resources.append("cycle")
            case "m" :
                resources.append("moon")
            case "n" :
                resources.append("nature")
            case "h" :
                resources.append("heart")
    return resources

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


def execute_move(user, move, chars):
    target = move[1]
    move = move[0]


def encounter(chars, enemies) :
    both = []
    both.extend(chars)
    both.extend(enemies)

    for i in range(len(chars)) :
        chars[i].resources = ""

    while len(enemies) > 0 :
        both = sort_by_speed(both)
        for i in range(len(both)) :
            if both[i] in chars :
                print(f"{both[i].name}'s tablet:")
                print_tablet(both[i].tablet)

                both[i].resources = both[i].resources + get_resources(both[i].tablet)
                print(f"{both[i].name}'s resources: {read_cost(both[i].resources)}")

                move = both[i].choose_move(both[i].resources, enemies)
                #both[i].resources = delete_cost(move[0].cost, both[i].resources)

            else :
                move = both[i].choose_move(chars)

            # move consists of (Move, Character/Enemy)
            execute_move(both[i], move, both)

            #dead check
            for j in range(len(both)) :                             
                if both[j].hp < 1 :
                    if both[j].speed < both[i].speed :
                        i -= 1
                    if both[j] in chars :
                        chars.remove(both[j])
                    else : 
                        enemies.remove(both[j])
                    both.remove(both[j])
                    j -= 1   

        if len(chars) > 0 :
            print("You lost.")

    print("You won!")

create_agatha()
create_sak_pixan()
create_you()

e1_enemies = [WindSpirit(), WindSpirit(), WindSpirit()]

print("First Encounter!")
encounter(characters, e1_enemies)

#finish reading move
#add the cover up stones n name them
#agatha, unable
#error handle selecting target
from Tablet_Cost_Resources import *
from Move_Rotate import *
from Character import *

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
                # both[i].resources = delete_cost(move[0].cost, both[i].resources) 
                # why is cost deletion commented? taken care of already? inspect test later

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

        if len(chars) == 0 :
            print("You lost.")

    print("You won!")

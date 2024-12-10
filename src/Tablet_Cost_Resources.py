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
                    print(" 〜", end = " ")
                case "cycle" :
                    print(" ○", end = " ")
                case "moon" :
                    print(" ☾", end = " ")
                case "nature" :
                    print(" ⚶", end = " ")
                case "heart" :
                    print(" ♡", end = " ")
        print("")

def generate_key(length) :
    key = ""
    chars = ["s","t","c","m","n","h"]
    for i in range(len(chars)*2) :
        chars.append("e")
    for i in range(length ** 2) :
        key = key + random.choice(chars)
    return key

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

def read_cost(cost):
    symbols = ""
    cost = sorted(cost)
    for i in range(len(cost)) :
        current = cost[i]
        match current :
                case "s" :
                    symbols += "☆ "
                case "t" :
                    symbols += "〜 "
                case "c" :
                    symbols += "○ "
                case "m" :
                    symbols += "☾ "
                case "n" :
                    symbols += "⚶ "
                case "h" :
                    symbols += "♡ "
    return symbols


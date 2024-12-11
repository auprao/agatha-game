# MoveExt("name", directed bool, dmg, enemy_targets. heal, team_targets, cost)

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

class Rotate :
    def __init__(self, name, times, team_targets, cost, move=None) :
        self.name = name
        self.times = times
        self.team_targets = team_targets
        self.cost = cost
        self.move = move

def execute_move(user, move, chars):
    target = move[1]
    move = move[0]
    # to be written!
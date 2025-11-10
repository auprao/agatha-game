class Move :
    def __init__(self, name, dmg, heal, cost, directed=True, enemy_targets=1, team_targets=1) :
        self.name = name
        self.directed = True
        self.dmg = dmg
        self.enemy_targets = 1
        self.selfdmg = heal
        self.team_targets = 1
        self.cost = cost
        self.directed = directed
        self.enemy_targets = enemy_targets
        self.team_targets = team_targets

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
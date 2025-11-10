class Effect :
    def __init__(self, name, count=None, on_hit=None, on_attacking=None, turn_end=None, turn_start=None) :
        self.name = name
        self.count = count # only decided when actually applied
        self.on_hit = on_hit
        self.on_attacking = on_attacking
        self.turn_end = turn_end
        self.turn_start = turn_start


# book of lambdas
actions = {
    "decay" : (lambda max_hp, hp, speed, count : (max_hp, hp - count, speed, count - 1)),
    "slowed" : (lambda max_hp, hp, speed, count : (max_hp, hp, speed - 1, count))
}


# book of effects
effects = {
    "burn" : Effect("Burning", turn_end=(lambda max_hp, hp, speed, count : (max_hp, hp - count, speed, count - 1))),
    "slowed" : Effect("Slowed", turn_start=(lambda max_hp, hp, speed, count : (max_hp, hp, speed - 1, 0)))
}

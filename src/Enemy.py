import random

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

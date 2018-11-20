from random import randint
class Goblin(object):
    def __init__(self,gold):
        self.name = "Goblin"
        self.health = randint(10,50)
        self.power = randint(1,5)
        self.gold = randint(10,20)
    def take_damage(self,amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def heal(self, health):
        self.health += randint(1,5)
    def powerup(self, power):
        self.power += randint(1,5)
    
        

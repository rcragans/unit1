from random import randint
class Vampire(object):
    def __init__(self,gold):
        randomPower = randint(5,10)
        self.name = "Vampire"
        self.health = randint(10,30)
        self.power = randomPower
        self.gold = randint(10,20)
    def take_damage(self,amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def heal(self, health):
        self.health += randint(5,10)
    def powerup(self, power):
        self.power += randint(5,10)
    
    
        


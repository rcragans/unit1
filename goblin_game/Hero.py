from random import randint
class Hero(object):
    def __init__(self,name,power,gold):
        self.name = name
        self.health = randint(10,50)
        self.power = randint(1,10)
        self.gold = gold
    def cheer_hero(self):
        print "Welcome brave %s" % (self.name)
    def take_damage(self,amount_of_damage):
        self.health -= amount_of_damage
    def is_alive(self):
        return self.health > 0
    def heal(self, health):
        self.health += randint(5,10)
    def powerup(self):
        self.power += randint(5,10)
    def use_potion(self):
        self.health += 10
   
    
    

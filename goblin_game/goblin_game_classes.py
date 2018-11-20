import os
import random
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
hero_name = raw_input("What is your name?")
theHero = Hero(hero_name,random.randint(10,20),0)
theHero.cheer_hero()


while (theHero.is_alive()):
    randMonster = random.randint(1,2)
    if randMonster == 1:
        monster = Goblin(random.randint(10,20))
    else:
        monster = Vampire(random.randint(10,20))
    print "You have encountered the terrifying %s" % monster.name
    while(theHero.is_alive() and monster.is_alive()):
        message = """
        You have %d health and %d power. 
        The %s has %d health and %d power.
        What do you want to do?
        1. fight %s
        2. dance
        3. flee
        4. use potion
        5. powerup""" 
        print message % (theHero.health, theHero.power,monster.name, monster.health, monster.power, monster.name)
        user_input = raw_input()
        if user_input == "1":
            monster.take_damage(theHero.power)
            print "You have done %d damage to the %s!" % (theHero.power, monster.name)
        elif user_input == "2":
            hero_health_increase = random.randint(5,7)
            theHero.health += hero_health_increase
            monster_health_increase = random.randint(1,5)
            monster_powerup = random.randint(1,5)
            monster.power += monster_powerup
            randAction = random.randint(1,2)
            if randAction == 1:
                action = monster.heal
                print "%s just gained %s health." % (monster.name, monster_health_increase)
            else:
                action = monster.powerup
                print "%s just powered up by %s power." % (monster.name, monster_powerup)
                print "The %s stares at you in disbelief of your stupidity. Little does he know, you just gained %d health." % (monster.name, hero_health_increase)
                print "Your health is now %d." % theHero.health
        elif user_input == "3":
            print "Goodbye, cowardly %s" % hero_name
            break
        elif user_input == "4":
            theHero.use_potion()
            print "Your health is now %d" % theHero.health
        elif user_input == "5":
            theHero.powerup()
            print "Your power is now %d" % theHero.power
        else:
            print "Thou fool. Thou hast stumbledeth (invalid input)."
        if monster.is_alive():
            theHero.take_damage(monster.power)
            print "The %s hits you for %d damage." % (monster.name, monster.power)
            if not theHero.is_alive():
                print "Thou hast been slain."
        if theHero.is_alive < 5:
            print "%s has gone into a rage as death approaches. Power increased!" % hero_name
            theHero.power += random.randint(10,20)
        if not monster.is_alive():
            hero_gold = 0
            monster.gold += theHero.gold
            print "You have %s gold." % theHero.gold
        raw_input("Hit enter to continue")
        os.system("clear")
        

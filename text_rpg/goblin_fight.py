import os
import random
hero_name = raw_input("What is thy name, brave adventurer? ")
def fight():
    print "Welcome, %s. Thou art brave!" % hero_name
    hero_health = random.randint(10,20)
    hero_power = random.randint(1,5)
    goblin_health = random.randint(10,20)
    goblin_power = random.randint(1,5)
    while  hero_health > 0 and goblin_health > 0:
        message = """You have %d health and %d power. 
        The goblin has %d health and %d power.
        What do you want to do?
        1. fight goblin
        2. dance
        3. flee""" 
        print message % (hero_health, hero_power, goblin_health, goblin_power)
        user_input = raw_input()
        if user_input == "1":
            goblin_health -= hero_power
            print "You have done %d damage to the goblin!" % hero_power
        elif user_input == "2":
            hero_health += 1
            print "The goblin stares at you in disbelief of your stupidity. Little does he know, you just gained 1 health."
            print "Your health is now %d." % hero_health
        elif user_input == "3":
            print "Goodbye, cowardly %s" % hero_name
            break
        else:
            print "Thou fool. Thou hast stumbledeth (invalid input)."
        if goblin_health > 0:
            hero_health -= goblin_power
            print "The goblin hits you for %d damage." % goblin_power
            if hero_health <= 0:
                print "Thou hast been slain."
        else:
            os.system("say Hooray! thou hast killed the goblin")
        if hero_health < 5:
            print "%s has gone into a rage as death approaches. Power increased!" % hero_name
            hero_power += 5
        raw_input("Hit enter to continue")
        os.system("clear")
fight()

import os
import time
import random
from Character import Character
import Monster
from Monster import Goblin, Vampire, Brigand, Wizard, Mermaid, Mountain_lion
from Monster import Ski_bunny, Whirling_dervish, Snake, Shark, Abominable_snowman
from Monster import Giant_scorpion, Sandworm, Mountain_troll, Beach_bunny, Zombie, Shadow, Medic


from Companion import Knight, Bard, Thief, Companion
from Item import Item
from Battle import Battle
from Hero import Hero



hero = Hero("myhero", 40, 25, "Mountains", "Hero")
a_goblin = Goblin("goblin", 10, 5, "Mountains", "Goblin")
a_vampire = Vampire( "vamp", 12, 8, "Mountains", "Vampire")
a_brigand = Brigand("brigand", 8, 2, "Mountains", "Brigand")


battle_engine = Battle()
#shopping_engine = Shopping()
monsters = [a_vampire, a_goblin, a_vampire, a_brigand]


for monster in monsters:
    hero_won = battle_engine.do_battle(hero, monster)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    # shopping_engine.do_shopping(hero)

print "YOU WIN!"




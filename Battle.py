from Character import Character
from Monster import Monster
from Item import Item
from Companion import Companion
from Monster import Goblin, Vampire, Brigand, Wizard, Mermaid, Mountain_lion
from Monster import Ski_bunny, Whirling_dervish, Snake, Shark, Abominable_snowman
from Monster import Giant_scorpion, Sandworm, Mountain_troll, Beach_bunny, Zombie, Shadow, Medic

from Companion import Knight, Bard, Thief

import time




class Battle(object):
    def __init__(self):
        battle_num = 1




    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.is_alive() and enemy.is_alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.is_alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

            
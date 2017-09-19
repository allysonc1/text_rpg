import os
import time
from random import randint
from Monster_generator import Monster_generator
from Character import Character
import Monster
from Monster import Goblin, Vampire, Brigand, Wizard, Mermaid 
from Monster import Ski_bunny, Whirling_dervish, Snake, Shark
from Monster import Giant_scorpion, Sandworm, Mountain_troll 
from Monster import Mountain_lion, Abominable_snowman, Zombie
from Monster import Beach_bunny, Shadow, Medic, Siren
from Companion import Knight, Bard, Thief, Companion
from Item import Item
from Battle import Battle
from Hero import Hero

global list_of_monster_types, list_of_regions

game_monsters = []
# Creates a list containing 3 lists, each item is another list
# w, h = 3, 11;
# regional_monsters = [[]]

list_of_monster_types = ["Goblin", 'Vampire', 'Brigand', "Wizard", "Mermaid", "Ski_bunny", "Whirling_dervish", "Snake", "Shark", "Giant_scorpion", "Sandworm", "Mountain_troll", "Mountain_lion", "Abominable_snowman", "Zombie", "Beach_bunny", "Shadow", "Medic", "Siren" ]
num_of_monster_types = len(list_of_monster_types)

list_of_regions = ["desert", "mountain", "ocean_beach"]

a = "Goblin"
b = exec(a + "()")
# game_monsters.append(b)
a = Vampire()
game_monsters.append(a)
a = Brigand()
game_monsters.append(a)
for i in range(0, 2):
	print game_monsters[i], "game_monsters", i

	# game_monsters.append(regional_monsters[i])
	# RETURNS SET OF MONSTERS 
# END FOR

# from characters import Hero, monster

# instantiate a hero object from the Hero class
the_hero = Hero("myhero", 40, 25, "mountain", "Hero")


# a_goblin = Goblin("goblin", 10, 5, "Mountains", "Goblin")
# a_vampire = Vampire( "vamp", 12, 8, "Mountains", "Vampire")
# a_brigand = Brigand("brigand", 8, 2, "Mountains", "Brigand")

# Make a list to hold all our monsters and give them names
monsters = []
names_of_monsters = ["Bert", "Sarah", "Ernie", 'Vlad', "Jerome", 'Jip', 'Spot', "Jeeves", "Merry", "Rita", "Bob", "Herzog", "Sawyer"]
num_names = len(names_of_monsters) - 1


# Before the game starts, let's ask the hero for his or her name.
print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")
the_hero.cheer_for_hero()
print " "
print "Where are you from, brave %s?" % the_hero.name
region_hero_is_from = (raw_input("> "))
print "%s sounds like an evil, scary place!" % region_hero_is_from
print " "



print "How many monsters are you willing to fight, brave %s?" % the_hero.name
number_of_enemies = int(raw_input("> "))

for i in range(0,number_of_enemies):
	rand_num = randint(1,3)
	if(rand_num == 1):
		monsters.append(Brigand(names_of_monsters[i]))
		names_of_monsters[i] = names_of_monsters[num_names]
		num_names -= 1
	elif(rand_num == 2):

		monsters.append(Vampire(names_of_monsters[i]))
		names_of_monsters[i] = names_of_monsters[num_names]
		num_names -= 1	

	elif(rand_num == 3):
		monsters.append(Goblin(names_of_monsters[i]))
		names_of_monsters[i] = names_of_monsters[num_names]
		num_names -= 1
	print monsters[i], "here be monsters"

	# END IF LOOP

# END FOR LOOP



# we need to loop through all the monsters!
for i,monster in enumerate(monsters):
	j = 0
	
	# Run the game as long as BOTH characters have health (are alive)
	while monster.is_alive() and the_hero.is_alive():
		# print monster
		# game is on!
		#os.system("clear") # CAN RUN SCRIPT COMMANDS "mkdir", "cd", etc.
		j += 1
		print " "
		print "Battle round, %d" % (j)
		print "You're confronting a %s named %s" % (monster.type_of_character, monster.name)
		print " "
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The %s named %s has %d health and %d power." % (monster.type_of_character, monster.name, monster.health, monster.power)
		print " "
		print "What do you want to do?"
		print "1. fight %s" % monster.name
		print "2. do nothing"
		print "3. flee"
		print "> "
		user_input = raw_input()
		if user_input == "1":
			# User has chosen to attack. 
			# Take away health from the monster based on hero power
			# monster_health -= hero_power
			# the monster class should be managing the monsters health
			# the hero is going to do the_hero.power damage to the monster
			monster.take_damage(the_hero.power)
			print "The hero is attacking!"
			if monster.is_alive():
				print "The %s is hit for %d damage." % (monster.type_of_character, the_hero.power)
				print "%s has %d health left" % (monster.name, monster.health)
			else:
				print "%s the poor %s is dead, you murderer!" % (monster.name, monster.type_of_character)

			# END IF LOOP

				

		elif user_input == "2":
			print "The hero stands there like an idiot."
			# Hero is going to stand there like an idiot
			pass
		elif user_input == "3":
			print "Goodbye, coward! You remind me of Goober."
			# os.system("say Goodbye, coward! You remind me of Goober.")
			# call break, to end the while loop
			break
		else:
			print "Invalid input %s" % user_input

		# END IF LOOP


			

		# monsters turn to attack!! (only if he's still alive)
		if monster.is_alive():
			# just like the monster, the hero should be changing its own stuff
			# so... call take_damage on the hero
			# hero_health -= monster_power
			the_hero.take_damage(monster.power)

			print "The %s named %s hits you for %d damage" % (monster.type_of_character, monster.name, monster.power)

		# END IF LOOP
			
		# monster has attacked, now check to see if hero is still alive...
		if the_hero.is_alive():
			print "You have %d health and %d power left." % (the_hero.health, the_hero.power)
		else:
			print "You have been killed by the weak monster. Shame on you."	

		# END IF LOOP


	# END WHILE LOOP

# END FOR LOOP


print "Game Over. Goodbye"
print " "
print " "

print " "
		
print " "









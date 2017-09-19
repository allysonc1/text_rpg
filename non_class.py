# this is a procedural approach to a text based rpg game
# the hero is going to fight a goblin
# the hero will have the options to:
# 1. fight the goblin
# 2. do nothing (goblin will still attack the hero)
# 3. run away


hero_health = 10
hero_power = 10
goblin_health = 6
goblin_power = 2

# run the game as long as both characters have health (are alive)
while goblin_health > 0 and hero_health > 0:
	print "game is on!"

	print "You have %d health and %d power." % (hero_health, hero_power) 
	print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
 	print "What do you want to do?"
 	print "1. fight goblin"
 	print "2. do nothing"
 	print "3. flee"
 	print "> ",
 	user_input = raw_input()
 	if user_input == '1':
 		# user has chosen to attack
 		#take away health from goblin based on hero power
 		print "goblin dies"
 		goblin_health -= hero_power
 	elif user_input == '2':
 		# hero does nothing
 		print "hero stands there like an idiot"
 		pass
 	elif user_input == '3':
 		# hero runs away
 		print "goodbye, coward. you remind me of goober."
 		break # call break, to end the while loop
 	else:
 		print 'invalid user input %s' % user_input

 	if goblin_health > 0:
 		hero_health -= goblin_power
 		print "the goblin hits you for %d damage" % goblin_power
 		# goblin has attacked
 		# is hero alive?
 		if hero_health <= 0:
 			print "you have been killed by the goblin. shame on you"
 		else:
 			print "try again, you're still hanging in there."





class Monster_generator(object):
	def __init__(self):


		enemies = []
		enemy_instances = []
		j = 0
		for i in range(0, len(list_of_monster_types) - 1):
			string1 = list_of_monster_types[i]()
			string2 = string1 + ".()"
			enemy_instances[i] = string2
			# string2
			print string1, string2, " str1 and str2"
			print enemy_instances[i], " enemy_instances"
			# if region == string2:
			# 	enemies[i][j] = list_of_monster_types[i]
			# 	print enemies[i][j]
			# 	j += 1



		# return enemies




		# monsters = []
		# names_of_monsters = ["Bert", "Sarah", "Ernie", 'Vlad', "Jerome", 'Jip', 'Spot', "Jeeves", "Merry", "Rita", "Bob", "Herzog", "Sawyer", "Spike", "Drusilla", "Buffy", "Gilligan", "Professor", "Ginger", "Mary_ann", "Snape", "Moonbeam", "Bob_lee", "Monther_of_Dragons", "Cersei", "Sugarbear", "Killjoy", "Sarah_conner", "Spacecat", "Indy", "Silverpuff", "Skipper", "Mrs_Howell", "Oneill", "Hamlet", "Homeybear", "Morris", "Sherlock", "John_watson", "AuntB", "Barney"]
		# num_names = len(names_of_monsters) - 1

		# for i in range(0,number_of_enemies):
		# 	rand_num = randint(1,3)
		# 	if(rand_num == 1):
		# 		monsters.append(Brigand(names_of_monsters[i], 8, 2, "Mountains", "Brigand"))
		# 		names_of_monsters[i] = names_of_monsters[num_names]
		# 		num_names -= 1
		# 	elif(rand_num == 2):

		# 		monsters.append(Vampire(names_of_monsters[i], 12, 8, "Mountains", "Vampire"))
		# 		names_of_monsters[i] = names_of_monsters[num_names]
		# 		num_names -= 1	

		# 	elif(rand_num == 3):
		# 		monsters.append(Goblin(names_of_monsters[i], 10, 5, "Mountains", "Goblin"))
		# 		names_of_monsters[i] = names_of_monsters[num_names]
		# 		num_names -= 1
		# 	print monsters[i]

	# END IF LOOP

# END FOR LOOP











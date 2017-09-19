
class Item(object):
	def __init__(self, owner):
		self.owner = owner
		self.effective_against = ["Goblin", "Brigand", "Vampire", "Wizard", "Whirling_dervish", 
		"Giant_scorpion", "Snake", "Sandworm", "Medic", "Shadow", "Mountain_lion", "Ski_bunny", 
		"Abominable_snowman", "Mountain_troll", "Mermaid", "Siren", "Shark", "Beach_bunny", "Hero"]

# item number 1
class Tonic(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Tonic'
		self.owner = owner
		self.effective_against = ["Hero"]

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 2

class Sword(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 10
		name = 'Sword'
		self.owner = owner
		self.effective_against = ["Medic", "Shadow", "Shark"]

	def apply(self, attacking_character, character_to_attack):
		flag = False
		for i in self.effective_against:
			if (character_to_attack.type_of_character == self.effective_against[i]):
				character_to_attack.health += attacking_character.power
				print "%s slices the %s with the Sword. Blood goes everywhere." % (attacking_character.name, character_to_attack.name)
				print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)
				flag = True

		if flag == False:
			print "Try your Sword on somebody else. It can't hurt this kind of monster. Better run!"



# item number 3

class Sleeping_potion(Item):
	def __init__(self, owner):
		super(Sleeping_potion, self).__init__(name)
		price = 5
		name = 'Sleeping_potion'
		self.owner = owner
		self.effective_against = ["Mountain_lion"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Mountain_lion"):
			print "Try the Sleeping_potion on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s throws the Sleeping_potion at the Mountain_lion and it instantly drops deeply asleep." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)



# item number 4

class Boots(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Boots'
		self.owner = owner
		self.effective_against = ["Snake"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Snake"):
			print "Try your Boots on somebody else. They won't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s stomps on the Snake with his Boots until the Snake screams." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)



# item number 5

class Healing_potion(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Healing_potion'
		self.owner = owner
		self.effective_against = ["Hero"]

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 6

class Snowboard(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Snowboard'
		self.owner = owner
		self.effective_against = ["Abominable_snowman"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Abominable_snowman"):
			print "Try the Snowboard on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s boards down the hill until it gets too hot for the Abominable_snowman and he starts frying in the sun." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)



# item number 7

class Invisibility_cloak(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Invisibility_cloak'
		self.owner = "Thief"
		self.effective_against = ["Hero"]

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 8

class Body_armor(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Body_armor'
		self.owner = owner
		self.effective_against = ["Hero"]

	
	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 9

class Wings(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Wings'
		self.owner = owner
		self.effective_against = ["Hero"]


	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 10

class Bow_and_arrow(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Bow_and_arrow'
		self.owner = owner

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 11

class Med_kit(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Med_kit'
		self.owner = "Medic"
		self.effective_against = ["Hero"]

	def apply(self, character_to_heal):
		character_to_heal.health += 6
		print "%s's health increased to %d." % (character_to_heal.name, character_to_heal.health)


# item number 12

class Supertonic(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Supertonic'
		self.owner = owner
		self.effective_against = ["Hero"]

	def apply(self, character_to_heal):
		character_to_heal.health += character_to_heal.max_health
		print "%s's health increased to %d. He's going to live! " % (character_to_heal.name, character_to_heal.health)


# item number 13

class Gold_pieces(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Gold_pieces'
		self.owner = owner

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 14

class Cave(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Cave'
		self.owner = "Landscape"

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 15

class Coconut_tree(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Coconut_tree'
		self.owner = "Landscape"

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 16

class Evade_points(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Evade_points'
		self.owner = owner

	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)


# item number 17

class Net(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Net'
		self.owner = owner
		self.effective_against = ["Giant_scorpion"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Giant_scorpion"):
			print "Try the net on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s throws the net over the Giant_scorpion. It tries to look very mean." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)


# item number 18

class Do_not_eat(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Do_not_eat'
		self.owner = owner
		self.effective_against = ["Sandworm"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Sandworm"):
			print "Try Do_not_eat on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health = 0
			print "%s tosses the Do_not_eat on the Sandworm and it shrivels up screaming, I'm melting!!." % attacking_character.name
			print "%s' died." % character_to_attack.name


# item number 19

class Rope(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Rope'
		self.owner = owner
		self.effective_against = ["Mountain_troll"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Mountain_troll"):
			print "Try the rope on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s ties the rope around the Mountain_troll. He can't get loose and starts crying for his mommy." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)



# item number 20

class Lift_ticket(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Lift_ticket'
		self.owner = owner
		self.effective_against = ["Ski_bunny"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Ski_bunny"):
			print "Try the Lift_ticket on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s climbs onto the lift with the Ski_bunny and at the highest point, throws her off the lift." % attacking_character.name
			print "She screams all the way down."
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)



# item number 21

class Red_gemstone(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Red_gemstone'
		self.owner = owner
		self.effective_against = ["Wizard"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Wizard"):
			print "Try this gem on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s holds up the Red_gemstone and mesmerizes the Wizard." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)



# item number 22

class Wooden_stake(Item):
	def __init__(self, owner):
		super(Item, self).__init__(name)
		price = 5
		name = 'Wooden_stake'
		self.owner = owner
		self.effective_against = ["Vampire"]

	def apply(self, attacking_character, character_to_attack):
		if (character_to_attack.type_of_character != "Vampire"):
			print "Try the Wooden_stake on somebody else. It can't hurt this kind of monster. Better run!"
		else:
			character_to_attack.health += attacking_character.power
			print "%s stabs the Vampire with the Wooden_stake. Blood goes everywhere." % attacking_character.name
			print "%s's health decreased to %d." % (character_to_attack.name, character_to_attack.health)







from Monster import Monster

class Vampire(Monster):
	def __init__(self, name, health, power):
		super(Vampire, self).__init__(name, health, power)
		self.type = "Vampire"
	

		# Character sets these variables and methods:
	# 	self.name = "Vampire"
	# 	self.health = 15
	# 	self.power = 4
	# def take_damage(self,amount_of_damage):
	# 	self.health -= amount_of_damage
	# def get_health(self):
	# 	return self.health
	# def is_alive(self):
	# 	return self.health > 0


	def make_girls_swoon(self):
		print "The skin of the vampire sparkles in the sunlight. You take 1 point damage."
		damage_done = -1
		return damage_done 
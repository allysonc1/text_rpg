from Monster import Monster

class Goblin(Monster):
	def __init__(self, name, health, power):
		super(Goblin, self).__init__(name, health, power)
		self.type = "Goblin"
	# 	self.name = 'Goblin'
	# 	self.health = 6
	# 	self.power = 2
	# def take_damage(self, amount_of_damage):
	# 	self.health -= amount_of_damage

	# define a method just for goblins
	def do_a_dance(self):
		print "The goblin does a dance and you are horrified and stupified, but take no damage."	
	
		
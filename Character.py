# This is our super class. all other characters will 
# be subclasses
class Character(object):
	def __init__(self, name, health, power, region, type_of_character):
		self.name = name
		self.health = health
		self.power = power
		self.pieces_of_gold = 20
		self.region = region
		self.type_of_character = type_of_character

	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage

	def get_health(self):
		return self.health

	def set_health(self, new_health):
		return self.health
	
	def get_name(self):
		return self.name

	def get_power(self):
		return self.power

	def get_pieces_of_gold(self):
		return self.pieces_of_gold

	def get_character_type(self):
		return self.type_of_character

	def is_alive(self):
		unfortunately_yes = (self.health > 0)
		return unfortunately_yes

	def attack(self, enemy):
		new_enemy_health = enemy.get_health()
		enemy.set_health(new_enemy_health - self.power)

	def print_status(self):
		print "%s has %d health and %d power." % (self.name, self.health, self.power)


# def attack(self, enemy):
	#     if not self.alive():
	#         return
	#     print "%s attacks %s" % (self.name, enemy.name)
	#     enemy.receive_damage(self.power)
	#     time.sleep(1.5)

	# def receive_damage(self, points):
	#     self.health -= points
	#     print "%s received %d damage." % (self.name, points)
	#     if self.health <= 0:
	#         print "%s is dead." % self.name

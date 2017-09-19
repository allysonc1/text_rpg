
from Character import Character

class Companion(Character):
	def __init__(self, name, health, power, region, type_of_character):
		super(Companion, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Companion"

class Knight(Companion):
	def __init__(self, name, health, power, region, type_of_character):
		super(Knight, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Knight"

class Bard(Companion):
	def __init__(self, name, health, power, region, type_of_character):
		super(Bard, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Bard"

	def sing_for_money():
		print "The bard plays and sings lovely songs for landowners."
		
class Thief(Companion):	
	def __init__(self, name, health, power, region, type_of_character):
		super(Bard, self).__init__(name, health, power, region, type_of_character)
		self.type_of_character = "Thief"
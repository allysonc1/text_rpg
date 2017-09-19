from Character import Character
from random import randint
# Create a Hero class
class Hero(Character):
	def __init__(self, name, health, power, region, type_of_character):
		super(Hero, self).__init__("Hero", 14, 5, "Mountains", "Hero")
		self.pieces_of_gold = 20
	
	def cheer_for_hero(self):
		print "Fight hard, valiant %s" % self.name

	def restore(self):
		self.health = 10
		print "Hero's heath is restored to %d!" % self.health
		time.sleep(1)

	def buy(self, item):
		self.coins -= item.cost
		item.apply(hero)

	def sell(self, item):
		self.coins += item.cost
	  #  item.apply(store). ?

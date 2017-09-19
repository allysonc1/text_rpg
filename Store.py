


class Shopkeeper(Character):
	def __init__(self, name, region, type_of_character):
		super(Shopkeeper, self).__init__(name, region, type_of_character)
		self.type_of_character = "Shopkeeper"
		self.region = "desert"
		self.name = "Bob"
		self.inventory = []


	def sell_item(self, item, buyer):
		if buyer.pieces_of_gold >= item.price:
			buyer.pieces_of_gold -= item.price
			item.owner = buyer
			self.pieces_of_gold += item.price
			# remove from inventory here as well
			print item, "has been transferred to you for %d" % item.price
			print "Thank you for your business."
		else:
			print "You don't have enough pieces_of_gold to purchase this item at this time."
			print "The price of this item is ", item.price

	def buy_item(self, item, seller):
		seller.pieces_of_gold += item.price - (item.price * .10)
		self.pieces_of_gold -= seller.pieces_of_gold
		item.owner = self
		# add to inventory
		self.inventory.append[item]
		print "The item has been transferred to my inventory and I have paid you %d pieces_of_gold" % pieces_of_gold
		print "Thank you for your business."

		


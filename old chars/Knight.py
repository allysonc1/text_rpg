from Companion import Companion 

class Knight(Companion):
	def __init__(self, name, health, power):
		super(Knight, self).__init__(name, health, power)
		self.type = "Knight"
	
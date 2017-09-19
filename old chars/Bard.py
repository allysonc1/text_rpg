from Companion import Companion 

class Bard(Companion):
	def __init__(self, name, health, power):
		super(Bard, self).__init__(name, health, power)
		self.type = "Bard"

	def sing_for_money():
		print "The bard plays and sings lovely songs for landowners."
		
	
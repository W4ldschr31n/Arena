from Arena.items.Item import Item

class Weapon(Item):

	def __init__(self, category='Fists', raw_damages=0):
		self.category = category
		self.raw_damages = raw_damages

	def getDamages(self):
		return self.raw_damages

	def __str__(self):
		return self.category

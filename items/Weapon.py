from items.Item import Item

class Weapon(Item):

	def __init__(self, name = 'Bare Hands', type='Fists', raw_damages=0):
		self.name = name
		self.type = type
		self.raw_damages = raw_damages

	def getDamages(self):
		return self.raw_damages

	def __str__(self):
		return self.name

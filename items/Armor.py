from Arena.items.Item import Item

class Armor(Item):

	def __init__(self, category ='Rags', defence=0):
		self.category = category
		self.defence = defence

	def protect(self, dmg):
		dmg = dmg - self.defence
		return dmg

	def __str__(self):
		return self.category



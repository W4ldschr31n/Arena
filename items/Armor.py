from .Item import Item

class Armor(Item):

	def __init__(self, name ='Rags', defence=0):
		self.name = name
		self.defence = defence

	def protect(self, dmg):
		dmg = dmg - self.defence
		return dmg

	def __str__(self):
		return self.name



from Arena.items.Item import HealingPotion

class Inventory():

	def __init__(self, items = None):
		self.items = [HealingPotion()] if items is None else items

	def addItem(self, item):
		self.items.append(item)

	def removeItem(self, item):
		self.items.remove(item)

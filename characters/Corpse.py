class Corpse():

	def __init__(self, character):
		self.items = [character.equipment.weapon, character.equipment.armor]
		self.items.extend(character.inventory.items)
		self.items = list(filter(lambda x:x is not None, self.items))
		self.name = character.name

	def __str__(self):
		return '%s (corpse): '%self.name + ','.join([str(i) for i in self.items]) if len(self.items) else 'Empty corpse'


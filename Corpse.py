class Corpse():
	def __init__(self, character):
		self.items = [character.weapon, character.armor]
		self.items.extend(character.belt)
		self.items = list(filter(lambda x:x is not None, self.items))
		self.name = character.name

	def __str__(self):
		return '%s (corpse): '%self.name + ','.join(map(lambda x:str(x), self.items)) if len(self.items) else 'Empty corpse'


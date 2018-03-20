class Item():
	def __init__(self):
		pass

class Consumable(Item):
	def __init__(self):
		pass

	def use(self):
		pass

class HealingPotion(Consumable):
	healParams={'lesser':5, 'normal':10, 'greater':15}

	def __init__(self, quality='normal'):
		self.quality = quality if quality in self.healParams else 'normal'
		self.heal = self.healParams[self.quality]

	def upgrade(self):
		qualities = sorted(self.healParams, key=lambda x:self.healParams[x])
		for i, q in enumerate(qualities):
			if q==self.quality and i<len(qualities)-1:
				self.quality  = qualities[i+1]
				self.heal = self.healParams[self.quality]
				break

	def use(self, character):
		assert character.isAlive(), 'Cannot heal a dead charater !'
		character.hp = min(character.hp+self.heal, character.maxHp)

	def __str__(self):
		return 'Healing potion (%s)'%self.quality

	def desc(self):
		return 'Heals for %d HP.'%self.heal

class Weapon(Item):
	pass

class Armor(Item):
	pass
